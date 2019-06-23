from os import path
from collections import defaultdict

import numpy

from excel_to_database.database_writer import DatabaseWriter
from excel_to_database.model import Person


HERE = path.abspath(path.dirname(__file__))
DATA = defaultdict(list, {'name': ['محمد'], 'family': ['خواجه زاده'], 'national_id': [1234567]})
DATA_WITH_EMPTY_FIELD = defaultdict(list, {'name': ['محمد'], 'family': [numpy.nan], 'national_id': [1234567]})
DATA_WITH_INVALID_FIELDS = defaultdict(list, {'name': ['محمد'], 'family': ['خواجه زاده'], 'national_id': ['Invalid']})


class TestDatabaseWriter:

    def test_database_writer(self, dbsession):

        db_writer = DatabaseWriter(dbsession, DATA, Person)
        db_writer.write_data_to_db()
        assert db_writer.get_final_result() is not None
        assert db_writer.get_final_result()['status'] is not None
        assert len(db_writer.get_final_result()['status']) == 1
        db_writer_for_empty_field = DatabaseWriter(dbsession, DATA_WITH_EMPTY_FIELD, Person)
        db_writer_for_empty_field.write_data_to_db()
        assert db_writer_for_empty_field.get_final_result() is not None
        assert db_writer_for_empty_field.get_final_result()['status'] is not None
        assert db_writer_for_empty_field.get_final_result()['status'][0] == 'Added'
        db_writer_for_invalid_field = DatabaseWriter(dbsession, DATA_WITH_INVALID_FIELDS, Person)
        db_writer_for_invalid_field.write_data_to_db()
        assert db_writer_for_invalid_field.get_final_result()['status'][0] == 'Failed'
