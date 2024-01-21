from scrapy.utils.project import get_project_settings
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def db_connect():
    return create_engine(get_project_settings().get('OBMEP_DATABASE_URL'))


def create_table(engine):
    Base.metadata.create_all(engine)


class City(Base):
    __tablename__ = 'city'

    edition = Column(String, primary_key=True)
    state_code = Column(String, primary_key=True)
    city = Column(String, primary_key=True)


class School(Base):
    __tablename__ = 'school'

    edition = Column(String, primary_key=True)
    state_code = Column(String, primary_key=True)
    city = Column(String, primary_key=True)
    school = Column(String, primary_key=True)
    school_type = Column(String)
    group = Column(String)


class Student(Base):
    __tablename__ = 'student'

    edition = Column(String, primary_key=True)
    level = Column(String, primary_key=True)
    name = Column(String, primary_key=True)
    school = Column(String, primary_key=True)
    school_type = Column(String)
    city = Column(String, primary_key=True)
    state_code = Column(String, primary_key=True)
    medal = Column(String)
    honorable_mention = Column(String)


class Teacher(Base):
    __tablename__ = 'teacher'

    edition = Column(String, primary_key=True)
    state_code = Column(String, primary_key=True)
    city = Column(String, primary_key=True)
    teacher = Column(String, primary_key=True)
    school = Column(String, primary_key=True)
    school_type = Column(String)
    group = Column(String)
