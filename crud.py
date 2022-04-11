from sqlalchemy.orm import Session
from models import Berita


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Berita).offset(skip).limit(limit).all()

def filter_title(db: Session, title: str):
    return db.query(Berita.title).filter(Berita.title == title).all()

def filter_date(db: Session, date: str):
    return db.query(Berita.date).filter(Berita.date == date).all()

def filter_category(db: Session, category: str):
    return db.query(Berita.category).filter(Berita.category == category).all()

def filter_website(db: Session, website: str):
    return db.query(Berita.website).filter(Berita.website == website).all()