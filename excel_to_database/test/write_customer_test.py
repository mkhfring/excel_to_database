from os import path
from excel_to_database.excel_reader import ExcelReader


HERE = path.abspath(path.dirname(__file__))


class ExcelReaderWithValidation(ExcelReader):

    def __init__(self, file_path):
        super().__init__(file_path)

    def validate_fields(self):
        for key, value in self.data.items():
            for index, element in enumerate(value):
                if key == 'کد ملی' and not self.validate_national_id(element):
                    value[index] = 'Invalid'

    @staticmethod
    def validate_national_id(national_id):
        if len(str(national_id)) != 10:
            return False

        return True


class TestExcelReader:

    def test_excel_reader(self, dbsession):
        excel_reader = ExcelReaderWithValidation(path.join(HERE, 'assets/practice.xlsx'))
        excel_reader.read_excel_data()
        excel_reader.validate_fields()
        assert excel_reader.get_data is not None
        data = excel_reader.get_data
        assert data['کد ملی'][2] == 'Invalid'
