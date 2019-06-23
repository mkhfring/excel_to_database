from collections import defaultdict

import pandas as pd
from excel_to_database.exeptions import ValidationException


class DatabaseWriter:

    def __init__(self, session, data, model):
        self.session = session
        self.data = data
        self.model = model
        self.status = []

    def write_data_to_db(self, translation: dict = None):
        translated_keys = None
        keys = [key for key in self.data.keys()]

        if translation:
            translated_keys = [translation[key] for key in keys]

        database_fields = translated_keys or keys

        if not all(key in dir(self.model) for key in database_fields):
            raise ValidationException('Fields of excel file does not match the database model')

        for index, _ in enumerate(self.data[keys[0]]):
            model_member = {
                translation[key] if translation else key: (
                    self.data[key][index] if not pd.isnull(self.data[key][index]) else None
                )
                for key in keys
            }
            if self.is_invalid_in_model_member(model_member):
                self.status.append('Failed')
                continue

            try:
                extended_model_member = self.extend_model_member(model_member)
            except NotImplementedError:
                extended_model_member = model_member

            try:
                is_exist = self.is_exist()
            except NotImplementedError:
                is_exist = False

            model = self.model(**extended_model_member)
            if is_exist:
                self.session.merge(model)
                self.session.commit()
                self.status.append('Updated')
            else:
                self.session.add(model)
                self.session.commit()
                self.status.append('Added')

    def get_final_result(self):
        self.data['status'] = self.status
        return self.data

    def extend_model_member(self, model_member, *args, **kwargs):
        raise NotImplementedError()

    def is_exist(self, *args, **kwargs):
        raise NotImplementedError

    @staticmethod
    def is_invalid_in_model_member(model_member):
        for value in model_member.values():
            if value == 'Invalid':
                return True

        return False

