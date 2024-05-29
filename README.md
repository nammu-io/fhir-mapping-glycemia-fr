**Mapping FHIR R4**

This repo is an example of how mapping data to FHIR format can be achieved. Follow the steps below.

1. Identify the FHIR resources:
   Identify which FHIR resources correspond to the data in your CSV file. Use a json file and place it in the repo.For example, Patient, Observation, etc. In this particular case, we use this particular example [https://interop.esante.gouv.fr/ig/fhir/mesures/3.0.1/Observation-ExampleMesObservationGlucose001.json.html] and we name the JSON file MesObservationGlucose.json

2. Place the data you want to map in the repo as a CSV file. In this case we use data from blood gucose sensor in the InputGlycemiaRawdata.csv file

3. Create a mapping:
   Define a mapping from your CSV data to the FHIR resources. This could be a simple 1-to-1 mapping or more complex transformations depending on your data. In the mapping.py file you will find an example in python. Create a folder output and modify the `mapping.py` script to define your specific mapping rules.

4. Transform the data:
   To use the `mapping.py`:
   - Run the script using the command `python mapping.py`.

The `mapping.py` script uses the mappings defined in the script to convert the CSV data into FHIR format.

There are several tools and libraries available that can help with this process. Here are a couple of GitHub repositories that might be useful:

- [toFHIR](https://github.com/srdc/tofhir): An easy-to-use data mapping and high-performant data transformation tool to transform existing datasets from various types of sources to HL7 FHIR.
- [FHIR-Converter](https://github.com/microsoft/FHIR-Converter): A conversion utility to translate legacy data formats into FHIR.
