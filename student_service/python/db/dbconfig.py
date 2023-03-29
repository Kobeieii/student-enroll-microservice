from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://admin:admin101@db:3306/devops_db')

Session = sessionmaker(bind=engine)
db = Session()
Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(200))

