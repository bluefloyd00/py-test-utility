# py-test-utility 

Contains a collection of class and functions which aim to help developers implement and test data pipelines against the new generation data warehouses and storing system i.e. BigQuery and GCS

## Installation
py-test-utility can be installed via pip

```python 
pip install py-test-utility
```
## mockdata - class csv_mock(csv,schema) 
Extract the equivalent json from csv with nested and repeated records structures

### Args

- csv
    - path and file name of the csv
    - mandatory
    - nested fields shall be separated by a dot "."  (i.e. item.id, item.quantity)

|order | item.id | item.quantity | delivery.address | delivey.postcode |
|---|---|---|---|---|
| A0001 | item1 | 5 | address1 | e13bp |
| | item2 | 1 | | |
| | item3 | 3 | | |
| A0002 | item4 | 4  | address4 | e13bp |
| | item1 | 4 | | |
| | item3 | 2 | | |

- schema 
    - path and schema file name of the table schema
    - required if the CSV contain nested and repeated records
    - json format i.e. 
```json
[  
    {
      "mode": "NULLABLE", 
      "name": "order", 
      "type": "STRING"
    },  
    {
      "fields": [
        {
          "mode": "NULLABLE", 
          "name": "id", 
          "type": "STRING"
        },
        {
          "mode": "NULLABLE", 
          "name": "quantity", 
          "type": "STRING"
        }
      ], 
      "mode": "REPEATED", 
      "name": "item", 
      "type": "RECORD"
    }, 
    {
      "fields": [
        {
          "mode": "NULLABLE", 
          "name": "address", 
          "type": "STRING"
        }, 
        {
          "mode": "NULLABLE", 
          "name": "postcode", 
          "type": "STRING"
        }
      ], 
      "mode": "NULLABLE", 
      "name": "delivery", 
      "type": "RECORD"
    }
  ]
```

### Methods
- to_json()
    - if successfuls return the json extracted from the csv


### Usage

```python 
>>> from mockdata import mockdata as md
>>> mockdata_csv = md.csv_mock(
...     csv="mockdata/test/data/csv/repeated_records.csv", 
...     schema="mockdata/test/schema/repeated_records_schema.json") # initialise the object
>>> mockdata_json = mockdata_csv.to_json() # return the equivalent json
```

