from excel_to_database.model import Person

class DatabaseWriter:

    def __init__(self, session, data, model):
        self.session = session
        self.data = data
        self.model = model

    def write_data_to_db(self, translation:dict = None):
        keys = [key for key in self.data.keys()]
        if translation:
            keys = [translation[key] for key in keys]

        if not all(key in dir(self.model) for key in keys):
            pass

        for index, _ in enumerate(self.data['کد ملی']):
            is_exist = self.session.query(self.model).filter(
                self.model.national_id == self.data['کد ملی'][index]
            ).one_or_none()
            model = self.model(

            )
            if is_exist:
                self.session.merge(model)
                self.session.commit()
            else:
                self.session.add(model)
                self.session.commit()
