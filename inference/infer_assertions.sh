#!/usr/bin bash

cp package/opencs.ttl.gz opencs2.ttl.gz;
gzip -d opencs2.ttl.gz ;
echo "extracted opencs ontology";

sed -i '/owl:imports <https:\/\/w3id.org\/ocs\/schema\/0.1.0>/a\    owl:imports <http://www.w3.org/2004/02/skos/core#> ;' opencs2.ttl ;
sed -i '/owl:imports <https:\/\/w3id.org\/ocs\/schema\//d' opencs2.ttl;
echo "deleted schema import, added skos import";

java -jar robot.jar merge --input opencs/schema/schema.ttl --input opencs2.ttl --output output_opencs.ttl;
echo "merged with schema";

java -jar robot.jar remove --input output_opencs.ttl --axioms tbox --output output_opencs.ttl;
java -jar robot.jar remove --input output_opencs.ttl --select "annotation-properties data-properties anonymous" --output output_opencs.ttl;
java -jar robot.jar remove --input output_opencs.ttl --select "<http://dbpedia.org/resource/*>" --output output_opencs.ttl;
java -jar robot.jar unmerge --input output_opencs.ttl --input opencs/inference/skos_patch.ttl --output output_opencs.ttl;
echo "removed unneccesary axioms ";

java -jar robot.jar reason --reasoner HermiT --axiom-generators "PropertyAssertion" --input output_opencs.ttl --output output_opencs2.ttl;
echo "reasoned";

java -jar robot.jar diff --left output_opencs.ttl --right output_opencs2.ttl | grep '\+' | awk '{print substr($0, 3)}' > inferred_assertions.ofn;
echo "inferred assertions";