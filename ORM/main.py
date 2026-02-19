from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column, Integer, String

URL = 'postgresql+psycopg2://postgres:13081981@localhost:5432/business'

engine = create_engine(URL, echo=True)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.age}'


Base.metadata.create_all(engine)

with Session() as session:
    new_row = User(name='Nurs', age=21)
    session.add(new_row)
    session.commit()
