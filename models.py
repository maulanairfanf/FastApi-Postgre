from sqlalchemy import  Column, String
from config import Base

class Berita(Base):
    __tablename__ ="berita"

    title = Column(String)
    date = Column(String)
    author = Column(String)
    link = Column(String, primary_key=True)
    category = Column(String)
    website = Column(String)
    content = Column(String)
