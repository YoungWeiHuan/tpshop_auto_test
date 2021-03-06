import json


def analyze_data(filename):
    with open('./data/' + filename, 'r', encoding='utf-8') as f:
        data_list = []
        for value in json.load(f).values():
            data_list.append(value)
    return data_list
