from rdflib import Graph, URIRef, Namespace
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib.namespace import SKOS, RDFS
import multiprocessing as mp
from aiohttp import ClientConnectorError
import pandas as pd
import pprint
import aiohttp
import time
import asyncio


def findwikiLink(dbpLink):
    sparql = SPARQLWrapper('http://dbpedia.org/sparql')
    sparql.setQuery( """SELECT ?wikiLink
    WHERE
    {
        <"""+str(dbpLink)+"""> owl:sameAs ?wikiLink.
        FILTER CONTAINS(str(?wikiLink),"wikidata")
    } """ )
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    if qres['results']['bindings']:
        return qres['results']['bindings'][0]['wikiLink']['value']
    else:
        return None

def getLocalLabel(localLink, graph):
    label = graph.objects(URIRef(localLink), SKOS.prefLabel)
    return str(next(label, None))


def getLabel(endpoint, link):                #  'https://query.wikidata.org/sparql'   'https://dbpedia.org/sparql/'
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery( """SELECT ?label
    WHERE
    {
        <"""+str(link)+"""> rdfs:label | skos:prefLabel | schema:name ?label.
        FILTER(lang(?label)='en')
    } """ )
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    r = qres['results']['bindings']
    if qres['results']['bindings']:
        return str( qres['results']['bindings'][0]['label']['value'] )
    else:
        return None

async def get_status(session, url):
    async with session.get(url) as r:
        return r.status

async def get_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_status(session,url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

async def main(urls):
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls)
        return data

if __name__ == '__main__':
    g = Graph()
    g.parse('opencs.ttl')

    # localConcepts = list()
    # dbpLinks = list()
    # for localConcept, dbpLink in g.subject_objects(SKOS.closeMatch):
    #     localConcepts.append(str(localConcept))
    #     dbpLinks.append(str(dbpLink))
    #
    #
    # pool = mp.Pool()
    # wikiLinks = pool.map(findwikiLink, dbpLinks)
    # d = { 'Local Link': localConcepts, 'DBpedia Link': dbpLinks, 'Wikidata Link': wikiLinks }
    # df = pd.DataFrame(d)
    # df.to_feather('test.feather')

    df = pd.read_feather('test.feather')
    pd.set_option('display.width', None)
    # print(df)




    # isDbpEq = []
    # isWikiEq = []
    # for index, row in df.iterrows():
    #     ll = getLocalLabel( row['Local Link'], g)
    #     dl = getLabel('https://dbpedia.org/sparql/', row['DBpedia Link'])
    #     wl = getLabel('https://query.wikidata.org/sparql', row['Wikidata Link'])
    #     if ll == None or dl == None:
    #         isDbpEq.append(None)
    #     elif ll.lower() == dl.lower():
    #         isDbpEq.append(True)
    #     else:
    #         isDbpEq.append(False)
    #
    #     if ll == None or wl == None:
    #         isWikiEq.append(None)
    #     elif ll.lower() == wl.lower():
    #         isWikiEq.append(True)
    #     else:
    #         isWikiEq.append(False)
    # print(isDbpEq)
    # print(isWikiEq)


    Dlink = df.iloc[0:100,1]
    lwLink = df[['Local Link','Wikidata Link']].head(100).dropna()
    Wlink = lwLink.iloc[:,1]
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    DlinkCode = asyncio.run(main(Dlink))
    WlinkCode = asyncio.run(main(Wlink))



    for i in range(len(DlinkCode)):
        if DlinkCode[i] == 200:
            g.add( ( URIRef( df.iloc[i,0]), SKOS.closeMatch, URIRef(df.iloc[i,1])  ) )
        else:
            g.remove(( URIRef( df.iloc[i,0]), SKOS.closeMatch, URIRef(df.iloc[i,1]) ))

    for i in range(len(WlinkCode)):
        if WlinkCode[i] == 200:
            g.add( ( URIRef(lwLink.iloc[i,0]), SKOS.closeMatch, URIRef(lwLink.iloc[i,1])  ) )
        else:
            g.remove(( URIRef(lwLink.iloc[i,0]), SKOS.closeMatch, URIRef(lwLink.iloc[i,1])  ))

    g.serialize('updatedOpenCS.ttl', format='ttl')