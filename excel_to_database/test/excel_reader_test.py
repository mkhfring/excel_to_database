from os import path
from excel_to_database.excel_reader import ExcelReader
from excel_to_database.database_writer import DatabaseWriter
from excel_to_database.model import Person


HERE = path.abspath(path.dirname(__file__))


class TestExcelReader:

    def test_excel_reader(self, dbsession):
        excel_reader = ExcelReader(path.join(HERE, 'assets/practice.xlsx'))
        data = excel_reader.read_excel_data()
        person = Person(name=data['نام'][0], family=data['نام خانوادگی'][0], national_id=data['کد ملی'][0])
        dbsession.add(person)
        dbsession.commit()
        assert data is not None
        assert 'نام' in data.keys()

        db_writer = DatabaseWriter(dbsession, data, Person)
        db_writer.write_data_to_db({'نام': 'name', 'نام خانوادگی': 'family', 'کد ملی': 'national_id'})
        assert db_writer.get_final_result() is not None
        assert db_writer.get_final_result()['status'] is not None
        assert len(db_writer.get_final_result()['status']) > 1

