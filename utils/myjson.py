import json


def get_data(path):
    jsonfile = open(path)
    data = json.load(jsonfile)
    jsonfile.close()
    return data
