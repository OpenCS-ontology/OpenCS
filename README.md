# OpenCS
Main OpenCS ontology repository.

The ontology is currently in its early stages of development. It was built from a subset of the [Microsoft Academic Knowledge Graph](https://makg.org/) by Michael Färber. You can find the scripts used for making OpenCS from MAKG in [this repository](https://github.com/OpenCS-ontology/makg-to-opencs).

See also **[the documentation](https://github.com/OpenCS-ontology/OpenCS/wiki/)** where you will find more information about the schema and ontology modules.

## Contents

- `/schema/schema.ttl` – OpenCS schema (upper ontology)
- `/ontology` – OpenCS ontology
  - `header.ttl` – header with ontology metadata
  - `authors.ttl` – manual list of ontology authors
  - `core` – core of the ontology, split into one Turtle file per concept. The files are grouped by 1000 into directories to help with potential filesystem or file browser issues.
  - `makg_extra.ttl.gz` – extra assertions carried over from MAKG
  - `opencs_to_makg.ttl.gz` – equivalence relations between OpenCS and MAKG
  - `shacl_constraints.ttl` – the file with SHACL constraints for ontology validation

## Releases
The `dev` release tag corresponds to the main branch in the repository and is updated automatically.

Tagged (versioned) releases are created manually and follow the [Semantic Versioning](https://semver.org/) scheme.

To create a new tagged release (example for version 1.2.3):
```sh
$ git checkout main
$ git pull
$ git tag v1.2.3
$ git push origin v1.2.3
```

The rest (packaging and release creation) will be handled automatically by the CI.

## License

The OpenCS ontology and all other contents of this repository are licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/).

## Authors

People who have contributed to OpenCS or the tools used to build or maintain it, in alphabetic username order.

- Anastasiya Danilenka ([@adanilenka](https://github.com/adanilenka))
- Aleksander Podsiad ([@AleksanderZawisza](https://github.com/AleksanderZawisza))
- Aleksandra Nawrocka ([@alexnawr](https://github.com/alexnawr))
- Arkadiusz Zalas ([@azalas](https://github.com/alexnawr))
- Krystian Kurek ([@KrystianKurek](https://github.com/KrystianKurek))
- Łukasz Pancer ([@luki139](https://github.com/luki139))
- Mateusz Kierznowski ([@mateuszkierznowski](https://github.com/mateuszkierznowski))
- Mikołaj Zalewski ([@mikolajzalewsk](https://github.com/mikolajzalewski))
- Mateusz Jastrzębiowski ([@mjastrzebiowski](https://github.com/mjastrzebiowski))
- Aleksandra Muszkowska ([@muszkowska](https://github.com/muszkowska))
- Nazira Tukeyeva ([@nazirait](https://github.com/nazirait))
- Piotr Sowiński ([@Ostrzyciel](https://github.com/Ostrzyciel))
- Przemysław Olender ([@przemekolender](https://github.com/przemekolender))
- Rafał Klimek ([@rklimek123](https://github.com/rklimek123))
- Paweł Golik ([@Shaveek23](https://github.com/Shaveek23))
- Dawid Przybyliński ([@Szwagi3r](https://github.com/Szwagi3r))
- Dominika Umiastowska ([@umiastowskad](https://github.com/umiastowskad))
- Paweł Wesołowski ([@wesolowskip](https://github.com/wesolowskip))
- Jan Wojtas ([@wojtas000](https://github.com/wojtas000))
- **The authors of the [Microsoft Academic Knowledge Graph](https://makg.org/)**, which OpenCS was initially derived from

### Maintainer
**Piotr Sowiński ([@Ostrzyciel](https://github.com/Ostrzyciel))**
