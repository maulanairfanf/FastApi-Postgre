from sqlalchemy import  Column, Integer, String
from config import Base

class Berita(Base):
    __tablename__ ="berita"

    title = Column(String)
    date = Column(String)
    author = Column(String)
    link = Column(Integer, primary_key=True)
    category = Column(String)
    website = Column(String)
    content = Column(String)
