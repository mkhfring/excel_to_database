from excel_to_database.exeptions import ValidationException


class DatabaseWriter:

    def __init__(self, session, data, model):
        self.session = session
        self.data = data
        self.model = model

    def write_data_to_db(self, translation: dict = None):
        translated_keys = None
        keys = [key for key in self.data.keys()]

        if translation:
            translated_keys = [translation[key] for key in keys]

        database_fields = translated_keys or keys

        if not all(key in dir(self.model) for key in database_fields):
            ValidationException('Fields of excel file does not match the database model')

        for index, _ in enumerate(self.data[keys[0]]):
            model_member = {translation[key]: self.data[key][index] for key in keys}
            try:
                extended_model_member = self.extend_model_member(model_member)
            except NotImplementedError as e:
                extended_model_member = model_member

            try:
                is_exist = self.is_exist()
            except NotImplementedError as e:
                is_exist = False

            model = self.model(**extended_model_member)
            if is_exist:
                self.session.merge(model)
                self.session.commit()
            else:
                self.session.add(model)
                self.session.commit()

    def extend_model_member(self, model_member, **kwargs):
        raise NotImplementedError()

    def is_exist(self, *args):
        raise NotImplementedError
