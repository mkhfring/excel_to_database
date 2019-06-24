from os import path
from excel_to_database.excel_reader import ExcelReader
from excel_to_database.database_writer import DatabaseWriter
from excel_to_database.model import Person


HERE = path.abspath(path.dirname(__file__))


class TestExcelReader:

    def test_excel_reader(self, dbsession):
        excel_reader = ExcelReader(path.join(HERE, 'assets/practice.xlsx'))
        excel_reader.read_excel_data()
        data = excel_reader.get_data
        assert data is not None
        assert 'نام' in data.keys()
        fields_translation = {'نام': 'name', 'نام خانوادگی': 'family', 'کد ملی': 'national_id'}
        db_writer = DatabaseWriter(dbsession, data, Person)
        db_writer.write_data_to_db(fields_translation)
        assert db_writer.get_final_result() is not None
        assert db_writer.get_final_result()['status'] is not None
        assert len(db_writer.get_final_result()['status']) > 1
