# py-test-utility 

Contains a collection of class and functions which aim to help deelopers in implementing and testing data pipelines against the new generation data warehouses and storing system i.e. BigQuery and GCS

## Installing
py-test-utility can be installed via pip

```python 
pip install py-test-utility
```
Or from the source code on GitHub.
```python
git clone --recurse-submodules https://github.com/bluefloyd00/py-test-utility
cd py-test-utility
pip install -U .
```

## mockdata module

### Class: from_csv(csv, schema) 

Takes in inpute csv file, table schema file and extract the json file, the csv can have nested fields and repeated nested records (return nested fields)

#### init - parameters

CSV
- path and file name of the csv
- mandatory
- nested fields shall be separated by a dot "."  (i.e. student.id, student.name)

SCHEMA 
- path and schema file name of the table schema
- required if the CSV contain nested and repeated records
- json format i.e. 
```json
[
    {
        "mode": "NULLABLE", 
        "name": "field1", 
        "type": "STRING"
    }, 
    {
        "mode": "NULLABLE", 
        "name": "field2", 
        "type": "STRING"
    }, 
    {
        "mode": "NULLABLE", 
        "name": "field3", 
        "type": "INTEGER"
    }
]
```

#### method to_json()
- if successful return the json extracted from the csv

### Usage

After inslling

#### example
```python 

import mockdata.mockdata as md
csv_mockdata = md.from_csv("mockdata/test/data/csv/repeated_records.csv", "mockdata/test/schema/repeated_records_schema.json")
        result = obj.to_json()
```
