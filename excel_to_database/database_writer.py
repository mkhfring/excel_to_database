from collections import defaultdict

import pandas as pd
from sqlalchemy.exc import IntegrityError

from excel_to_database.exeptions import ValidationException


class DatabaseWriter:

    def __init__(self, session, data, model):
        self.session = session
        self.data = data
        self.model = model
        self.status = []
        self.extra_info = []

    def write_data_to_db(self, translation: dict = None):

        keys = [key for key in self.data.keys()]

        for index, _ in enumerate(self.data[keys[0]]):
            model_member = {
                translation[key.strip()] if translation else key: (
                    self.data[key][index] if not pd.isnull(self.data[key][index]) else None
                )
                for key in keys
            }
            if self.is_invalid_in_model_member(model_member):
                self.status.append('Failed')
                self.extra_info.append('Invalid data in form')
                continue

            try:
                extended_model_member = self.extend_model_member(model_member)
            except NotImplementedError:
                extended_model_member = model_member

            if not all(key in dir(self.model) for key in extended_model_member):
                raise ValidationException('Fields of excel file does not match the database model')

            # TODO: check hassattr to evoid this rediculous try/except
            try:
                is_extra_model_valid = self.validate_extended_model(extended_model_member)
            except NotImplementedError as e:
                raise e

            model = self.model(**extended_model_member)
            existing_entity = self.get_user_if_exist(model)
            if existing_entity:
                try:

                    self.session.query(self.model).filter(
                        self.model.national_id == existing_entity.national_id
                    ).update(extended_model_member)
                    self.session.commit()
                    self.status.append('Updated')
                    if extended_model_member['peer_id'] is None:
                        self.extra_info.append('The entry is not registered in bale')
                    else:
                        self.extra_info.append('Normal')

                except IntegrityError as ie:
                    self.extra_info.append('The entry is already in database')
                    self.status.append('Failed')

                except Exception as e:
                    self.extra_info.append('Database operation failed')
                    self.status.append('Failed')

            else:
                try:

                    self.session.add(model)
                    self.session.commit()

                    self.status.append('Added')
                    if extended_model_member['peer_id'] is None:
                        self.extra_info.append('The entry is not registered in bale')
                    else:
                        self.extra_info.append('Normal')

                except IntegrityError as ie:
                    self.extra_info.append('The entry is already in database')
                    self.status.append('Failed')

                except Exception as e:
                    self.extra_info.append('Database operation failed')
                    self.status.append('Failed')

    def get_final_result(self):
        self.data['database status'] = self.status
        self.data['extra_information'] = self.extra_info
        return self.data

    def extend_model_member(self, model_member, *args, **kwargs):
        raise NotImplementedError()

    def get_user_if_exist(self, *args):
        raise NotImplementedError

    def validate_extended_model(self, extended_model):
        raise NotImplementedError

    @staticmethod
    def is_invalid_in_model_member(model_member):
        for value in model_member.values():
            if value == 'Invalid':
                return True

        return False
