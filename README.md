# py-test-utility 

Contains a collection of class and functions which aim to help deelopers in implementing and testing data pipelines against the new generation data warehouses and storing system i.e. BigQuery and GCS

## Installing
py-test-utility can be installed via pip

```python 
pip install py-test-utility
```
Or from the source code on GitHub.
```command line
git clone --recurse-submodules https://github.com/bluefloyd00/py-test-utility
cd py-test-utility
pip install -U .
```
## Dependencies

| Packages |
|---|
| pandas |
| types |
| json |
| csv |

## mockdata module

### Class: from_csv(csv, schema) 

Takes in inpute csv file, table schema file and return the equivalent json file from the csv - the csv can have nested fields and repeated nested records.

#### Parameters

csv
- path and file name of the csv
- mandatory
- nested fields shall be separated by a dot "."  (i.e. student.id, student.name)

|order | item.id | item.quantity | delivery.address | delivey.postcode |
|---|---|---|---|---|
| A0001 | item1 | 5 | address1 | e13bp |
| | item2 | 1 | | |
| | item3 | 3 | | |
| A0002 | item4 | 4  | address4 | e13bp |
| | item1 | 4 | | |
| | item3 | 2 | | |

schema 
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

#### example
```python 

import mockdata.mockdata as md
# initialise the object 
mockdata_csv = md.from_csv( "mockdata/test/data/csv/repeated_records.csv", 
                            "mockdata/test/schema/repeated_records_schema.json")
                            
result = mockdata_csv.to_json()
```
