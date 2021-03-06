from collections import defaultdict

import pandas


class ExcelReader:

    def __init__(self, file_path):
        self.file = file_path
        self.data = defaultdict(list)

    def read_excel_data(self):
        data_frame = pandas.read_excel(self.file)
        keys = data_frame.keys()
        for value_list in data_frame.values:
            for index, value in enumerate(value_list):
                self.data[keys[index]].append(value)

    def validate_fields(self):
        raise NotImplementedError()

    @property
    def get_data(self):
        return self.data
