from collections import defaultdict

import pandas


class ExcelReader:

    def __init__(self, file_path):
        self.file = file_path

    def read_excel_data(self):
        data_frame = pandas.read_excel(self.file)
        keys = data_frame.keys()
        data = defaultdict(list)
        for value_list in data_frame.values:
            for index, value in enumerate(value_list):
                data[keys[index]].append(value)

        return data

    def validate_fields(self, data: dict):
        raise NotImplementedError()

