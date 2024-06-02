from FakeRepository import FakeRepository



class SqlAlchemyRepository(FakeRepository):
    def __init__(self, session):
        self.session = session

    def add(self, item):
        self.session.add(item)

    def remove(self, item):
        self.session.delete(item)

    def get_all(self, model_class):
        items = self.session.query(model_class).all()
        return items

    def get_by_id(self, model_class, id):
        item = self.session.query(model_class).filter_by(id=id).first()
        return item