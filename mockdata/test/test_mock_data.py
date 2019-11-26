import unittest
import os
import types
import json
import pandas as pd
import csv
import mockdata.functions as fx
import mockdata.mockdata as md


class test_functions(unittest.TestCase):


    def test_is_repeated_record(self): 
        test_row = pd.Series(['nan', '2019-05-07 11:59:10 UTC', 'EUR', 'IT', 'delivery', 'DELIVERY_CHARGE', 1, 'aaa', 
                        1, 3920, 4900, 3920 , 4900 ], 
                    index =['order_reference', 'order_placement_time', 'currency', 'store_code', 'charges.type',
                            'charges.sku', 'charges.qty', 'product.type', 'product.qty', 'charges.unit_price.ex',
                            'charges.unit_price.inc', 'charges.list_price.ex', 'charges.list_price.inc' ])
        expected_result = False
        assert fx.is_repeated_record(test_row) == expected_result , "is_repeated_record negative result"

        test_row = pd.Series(['nan', 'nan', 'nan', 'nan', 'delivery', 'DELIVERY_CHARGE', 1, 'aaa', 
                        1, 3920, 4900, 3920 , 4900 ], 
                    index =['order_reference', 'order_placement_time', 'currency', 'store_code', 'charges.type',
                            'charges.sku', 'charges.qty', 'product.type', 'product.qty', 'charges.unit_price.ex',
                            'charges.unit_price.inc', 'charges.list_price.ex', 'charges.list_price.inc' ])
        expected_result = True
        assert fx.is_repeated_record(test_row) == expected_result , "is_repeated_record positive result"


    def test_add_column(self):           
        test_obj = {}
        test_field = "test1.test2"
        test_value = 5
        record_list = []
        expected_dict = {'test1': {'test2': 5}}
        # print(add_column(test_obj, test_field, test_value, record_list))
        assert fx.add_column(test_obj, test_field, test_value, record_list) == expected_dict, "add_column dict as input and 2 levels field"

            
        test_obj = []
        test_field = "test1.test2"
        test_value = 5
        record_list = []
        expected_dict = [{'test1': {'test2': 5}}]
        # print("{} equal {}".format( add_column(test_obj, test_field, test_value, record_list), expected_dict ))
        assert fx.add_column(test_obj, test_field, test_value, record_list)[0] == expected_dict[0] , "add_column - list as input and 2 levels field"
            
        test_obj = []
        test_field = "test1.test2.test3"
        test_value = 5
        record_list = ['test2']
        expected_dict = [{'test1': {'test2': [{'test3': 5}]}}]
        # print("{} equal {}".format( add_column(test_obj, test_field, test_value, record_list), expected_dict ))
        assert fx.add_column(test_obj, test_field, test_value, record_list)[0] == expected_dict[0] , "add_column - list as input and 3 levels field"

    def test_add_non_leaf(self):
        test_obj = {}
        test_field = "test4"
        expected_dict = {"test4" : {}}
        assert fx.add_non_leaf(test_obj, test_field) == expected_dict, "add_non_leaf - insert dict"

        test_obj = {}
        test_field = "test4"
        test_value = {}
        record_list = ['test4']
        expected_dict = {"test4" : [{}]}
        # print(add_non_leaf(test_obj, test_field, test_value, record_list))
        assert fx.add_non_leaf(test_obj, test_field, record_list) == expected_dict, "add_non_leaf - insert list of dict"


    def test_add_leaf(self):
        test_obj = {}
        test_field = "test4"
        test_value = 3
        expected_dict = {"test4" : 3}
        # print(fx.add_leaf(test_obj, test_field, test_value))
        assert fx.add_leaf(test_obj, test_field, test_value) == expected_dict, "add_leaf - insert key value"

    def test_is_record_field(self):
        l1 = ['charges', 'test2', 'test3']
        l2 = ['charges', 'product']
        assert fx.is_record_field(l1, l2) == True , "is_record_field: True"

        l1 = ['charges', 'test2', 'test3']
        l2 = ['charges1', 'product1']
        assert fx.is_record_field(l1, l2) == False , "is_record_field: False"

    def test_load_dictionary(self): 
        test_dictionary_list = [] 
        test_row = pd.Series([1.9e+09, '2019-05-07 11:59:10 UTC', 'EUR', 'IT', 'delivery', 'DELIVERY_CHARGE', 1, 'aaa', 
                        1, 3920, 4900, 3920 , 4900 ], 
                    index =['order_reference', 'order_placement_time', 'currency', 'store_code', 'charges.type',
                            'charges.sku', 'charges.qty', 'product.type', 'product.qty', 'charges.unit_price.ex',
                            'charges.unit_price.inc', 'charges.list_price.ex', 'charges.list_price.inc' ]) 
        record_list = ['test2']
        expected_dict = {'order_reference': 1900000000.0, 'order_placement_time': '2019-05-07 11:59:10 UTC', 
                        'currency': 'EUR', 'store_code': 'IT', 'charges': {'type': 'delivery', 'sku': 'DELIVERY_CHARGE',
                        'qty': 1, 'unit_price': {'ex': 3920, 'inc': 4900}, 'list_price': {'ex': 3920, 'inc': 4900}}, 
                        'product': {'type': 'aaa', 'qty': 1}}
        # print(json.dumps(load_dictionary(test_row, record_list), indent=4))
        # print(load_dictionary(test_row, record_list))
        self.assertEqual( fx.load_dictionary(test_dictionary_list, test_row, record_list)[0] , expected_dict , "load_dict"  )



        test_dictionary_list = []
        test_row = pd.Series([1.9e+09, '2019-05-07 11:59:10 UTC', 'EUR', 'IT', 'delivery', 'DELIVERY_CHARGE', 1, 'aaa', 
                        1, 3920, 4900, 3920 , 4900 ], 
                    index =['order_reference', 'order_placement_time', 'currency', 'store_code', 'charges.type',
                            'charges.sku', 'charges.qty', 'product.type', 'product.qty', 'charges.unit_price.ex',
                            'charges.unit_price.inc', 'charges.list_price.ex', 'charges.list_price.inc' ]) 
        record_list = ['charges', 'product']
        expected_dict = {'order_reference': 1900000000.0, 'order_placement_time': '2019-05-07 11:59:10 UTC', 
                        'currency': 'EUR', 'store_code': 'IT', 'charges': [{'type': 'delivery', 'sku': 'DELIVERY_CHARGE',
                        'qty': 1, 'unit_price': {'ex': 3920, 'inc': 4900}, 'list_price': {'ex': 3920, 'inc': 4900}}], 
                        'product': [{'type': 'aaa', 'qty': 1}]}
        # print(json.dumps(load_dictionary(test_row, record_list), indent=4))
        # print(load_dictionary(test_row, record_list))
        self.assertCountEqual( fx.load_dictionary(test_dictionary_list, test_row, record_list)[0] , expected_dict , "load_dict with lists"  )

        test_dictionary_list = [{'order_reference': 1900000000.0, 'order_placement_time': '2019-05-07 11:59:10 UTC', 
                        'currency': 'EUR', 'store_code': 'IT', 'charges': [{'type': 'delivery', 'sku': 'DELIVERY_CHARGE',
                        'qty': 1, 'unit_price': {'ex': 3920, 'inc': 4900}, 'list_price': {'ex': 3920, 'inc': 4900}}], 
                        'product': [{'type': 'aaa', 'qty': 1}]}]
        test_row = pd.Series(['nan', '2019-05-07 11:59:10 UTC', 'EUR', 'IT', 'delivery', 'DELIVERY_CHARGE', 1, 'aaa', 
                        1, 3920, 4900, 3920 , 4900 ], 
                    index =['order_reference', 'order_placement_time', 'currency', 'store_code', 'charges.type',
                            'charges.sku', 'charges.qty', 'product.type', 'product.qty', 'charges.unit_price.ex',
                            'charges.unit_price.inc', 'charges.list_price.ex', 'charges.list_price.inc' ]) 
        record_list = ['charges', 'product']
        expected_list_dict = [{'order_reference': 1900000000.0, 'order_placement_time': '2019-05-07 11:59:10 UTC', 'currency': 'EUR', 'store_code': 'IT', 'charges': [{'type': 'delivery', 'sku': 'DELIVERY_CHARGE', 'qty': 1, 'unit_price': {'ex': 3920, 'inc': 4900}, 'list_price': {'ex': 3920, 'inc': 4900}}], 'product': [{'type': 'aaa', 'qty': 1}]}, {'order_reference': 'nan', 'order_placement_time': '2019-05-07 11:59:10 UTC', 'currency': 'EUR', 'store_code': 'IT', 'charges': [{'type': 'delivery', 'sku': 'DELIVERY_CHARGE', 'qty': 1, 'unit_price': {'ex': 3920, 'inc': 4900}, 'list_price': {'ex': 3920, 'inc': 4900}}], 'product': [{'type': 'aaa', 'qty': 1}]}]
        # print(json.dumps(load_dictionary(test_dictionary_list, test_row, record_list), indent=4))
        # print(json.dumps(test_dictionary_list, indent=4))
        # print(load_dictionary(test_dictionary_list, test_row, record_list))
        
        self.assertCountEqual( fx.load_dictionary(test_dictionary_list, test_row, record_list), expected_list_dict , "load_dict load two dicts"  )
        


        test_dictionary_list = [{'order_reference': 1900000000.0, 'order_placement_time': '2019-05-07 11:59:10 UTC', 
                        'currency': 'EUR', 'store_code': 'IT', 'charges': [{'type': 'delivery', 'sku': 'DELIVERY_CHARGE',
                        'qty': 1, 'unit_price': {'ex': 3920, 'inc': 4900}, 'list_price': {'ex': 3920, 'inc': 4900}}], 
                        'product': [{'type': 'aaa', 'qty': 1}]}]
        test_row = pd.Series(['nan', 'nan', 'nan', 'nan', 'delivery', 'DELIVERY_CHARGE', 1, 'aaa', 
                        1, 3920, 4900, 3920 , 4900 ], 
                    index =['order_reference', 'order_placement_time', 'currency', 'store_code', 'charges.type',
                            'charges.sku', 'charges.qty', 'product.type', 'product.qty', 'charges.unit_price.ex',
                            'charges.unit_price.inc', 'charges.list_price.ex', 'charges.list_price.inc' ]) 
        record_list = ['charges', 'product']
        expected_list_dict = [{'order_reference': 1900000000.0, 'order_placement_time': '2019-05-07 11:59:10 UTC', 'currency': 'EUR', 'store_code': 'IT', 'charges': [{'type': 'delivery', 'sku': 'DELIVERY_CHARGE', 'qty': 1, 'unit_price': {'ex': 3920, 'inc': 4900}, 'list_price': {'ex': 3920, 'inc': 4900}}, {'type': 'delivery', 'sku': 'DELIVERY_CHARGE', 'qty': 1, 'unit_price': {'ex': 3920, 'inc': 4900}, 'list_price': {'ex': 3920, 'inc': 4900}}], 'product': [{'type': 'aaa', 'qty': 1}, {'type': 'aaa', 'qty': 1}]}]
        # print(json.dumps(load_dictionary(test_dictionary_list, test_row, record_list), indent=4))
        # print(json.dumps(expected_list_dict, indent=4))
        # print( load_dictionary(test_dictionary_list, test_row, record_list))
        # print(expected_list_dict[0])
        self.assertCountEqual( fx.load_dictionary(test_dictionary_list, test_row, record_list)[0] , expected_list_dict[0] , "load_dict load REPEATED dict"  )


    def test_load_record_list(self):
        list_records = fx.extract_repeated_records("mockdata/test/schema/ord_placed_test.json")
        self.assertCountEqual( list_records , [ 'products', 'collection_point', 'deliveries', 'charges'], "test_load_record_list - exract repeated record list from schema file")

class test_mockdata(unittest.TestCase):

    def test_class_csv_from(self):
        obj = md.csv_mock("mockdata/test/data/csv/simple.csv", "mockdata/test/schema/simple_schema.json")
        result = obj.to_json()
        with open("mockdata/test/data/json/simple.json", "r") as expected_file:
            expected = json.load(expected_file)
        self.assertCountEqual(result, expected, "to_json simple test")

        obj = md.csv_mock("mockdata/test/data/csv/repeated_records.csv", "mockdata/test/schema/repeated_records_schema.json")
        result = obj.to_json()
        with open("mockdata/test/data/json/repeated_records.json", "r") as expected_file:
            expected = json.load(expected_file)
        self.assertEqual(result, expected, "to_json repeated records")


if __name__ == "__main__":
    unittest.main()