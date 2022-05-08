import csv
import json


def csv_to_json(csv_file_path, json_file_path):
    json_array = []

    # read csv file
    with open(csv_file_path, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvreader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvreader:
            # add this python dict to json array
            json_array.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        json_string = json.dumps(json_array, indent=4)
        jsonf.write(json_string)


csvFilePath = r'categories.csv'
jsonFilePath = r'categories.json'
csv_to_json(csvFilePath, jsonFilePath)
