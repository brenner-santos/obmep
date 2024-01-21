from scrapy.utils.project import get_project_settings
from sqlalchemy import Column, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import BOOLEAN, DATETIME, NCHAR, NVARCHAR, SMALLINT

Base = declarative_base()


def db_connect():
    return create_engine(get_project_settings().get('OBMEP_DATABASE_URL'))


def create_table(engine):
    Base.metadata.create_all(engine)


class City(Base):
    __tablename__ = 'city'

    edition = Column(NVARCHAR(20), primary_key=True)
    state_code = Column(NCHAR(2), primary_key=True)
    city = Column(NVARCHAR(30), primary_key=True)
    created_at = Column(DATETIME, nullable=False)


class School(Base):
    __tablename__ = 'school'

    edition = Column(NVARCHAR(20), primary_key=True)
    state_code = Column(NCHAR(2), primary_key=True)
    city = Column(NVARCHAR(30), primary_key=True)
    school = Column(NVARCHAR(100), primary_key=True)
    school_type = Column(NCHAR(1), nullable=False)
    group = Column(NCHAR(2))
    created_at = Column(DATETIME, nullable=False)


class Student(Base):
    __tablename__ = 'student'

    edition = Column(NVARCHAR(20), primary_key=True)
    level = Column(SMALLINT, primary_key=True)
    name = Column(NVARCHAR(100), primary_key=True)
    city = Column(NVARCHAR(30), primary_key=True)
    state_code = Column(NCHAR(2), primary_key=True)
    school = Column(NVARCHAR(100), primary_key=True)
    school_type = Column(NCHAR(1), nullable=False)
    medal = Column(NVARCHAR(10))
    honorable_mention = Column(BOOLEAN)
    created_at = Column(DATETIME, nullable=False)


class Teacher(Base):
    __tablename__ = 'teacher'

    edition = Column(NVARCHAR(20), primary_key=True)
    state_code = Column(NCHAR(2), primary_key=True)
    city = Column(NVARCHAR(30), primary_key=True)
    teacher = Column(NVARCHAR(100), primary_key=True)
    school = Column(NVARCHAR(100), primary_key=True)
    school_type = Column(NCHAR(1), nullable=False)
    group = Column(SMALLINT)
    created_at = Column(DATETIME, nullable=False)
