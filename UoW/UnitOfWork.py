from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from AbstractUnitOfWork import AbstractUoW
from ..Repository.SQLAlchemyRepository import SqlAlchemyRepository


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine("sqlite:///training_diary.db")
)


class SqlAlchemyUnitOfWork(AbstractUoW):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.repository = SqlAlchemyRepository(self.session)

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()