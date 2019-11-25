import types
import json
import pandas as pd
import csv
import mockdata.functions as fx

class from_csv():
    def __init__(self, csv, schema):
        self.file_name = csv
        self.schema_file = schema
    
    def to_json(self):
        record_list = fx.extract_repeated_records(self.schema_file)
        # print(" ******************* {} ************************".format(record_list))
        df = pd.read_csv(self.file_name)
        df = df.where(pd.notnull(df), None)
        return fx.extract_list_dictionary(df, record_list)

if __name__ == "__main__":
    file_name = input("please insert the csv File Name: ")
    schema_file_name = input("please insert the schema File Name: ")
    output_json = input("please insert the json output File Name: ")
    f= open(output_json,"w+")
    csv_file = from_csv(file_name, schema_file_name)
    extracted_json = csv_file.to_json()
    f.write(json.dumps(extracted_json))
    print(json.dumps(extracted_json, indent=4))