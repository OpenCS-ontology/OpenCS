# OpenCS
Main OpenCS ontology repository.

The ontology is currently in its very early stages. It was built from a subset of the [Microsoft Academic Knowledge Graph](https://makg.org/) by Michael Färber. You can find the scripts used for making OpenCS from MAKG in [this repository](https://github.com/OpenCS-ontology/makg-to-opencs).

See also **[the documentation](https://github.com/OpenCS-ontology/OpenCS/wiki/)** where you will find more information about the schema and ontology modules.

## Contents

- `/schema/schema.ttl` – OpenCS schema (upper ontology)
- `/ontology` – OpenCS ontology
  - `header.ttl` – header with ontology metadata
  - `core` – core of the ontology, split into one Turtle file per concept. The files are grouped by 1000 into directories to help with potential filesystem or file browser issues.
  - `makg_extra.ttl.gz` – extra assertions carried over from MAKG
  - `opencs_to_makg.ttl.gz` – equivalence relations between OpenCS and MAKG

## License

The OpenCS ontology and all other contents of this repository are licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/).

## Authors

- [Piotr Sowiński](https://github.com/Ostrzyciel)
- The authors of the [Microsoft Academic Knowledge Graph](https://makg.org/)
