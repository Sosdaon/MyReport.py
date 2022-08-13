from flask_login import UserMixin


class RestorerLogin(UserMixin):
    def from_data_base(self, restorer_id, db):
        self.__restorer = db.get_restorer(restorer_id)
        return self

    def create(self, restorer):
        self.__restorer = restorer
        return self

    def get_id(self):
        return str(self.__restorer['id'])

    def get_name(self):
        return str(self.__restorer['restorer_name'])
