from os import path
from excel_to_database.excel_reader import ExcelReader


HERE = path.abspath(path.dirname(__file__))


class TestExcelReader:

    def test_excel_reader(self):
        excel_reader = ExcelReader(path.join(HERE, 'assets/practice.xlsx'))
        data = excel_reader.read_excel_data()

        assert data is not None
        assert 'نام' in data.keys()

