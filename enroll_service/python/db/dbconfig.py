from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://admin:admin101@db:3306/devops_db')

Session = sessionmaker(bind=engine)
db = Session()
Base = declarative_base()

class Enroll(Base):
    __tablename__ = 'enroll'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    subjectid = Column(String(255))
    term = Column(String(200))
    year = Column(Integer)