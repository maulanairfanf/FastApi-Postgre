from sqlalchemy.orm import Session
from models import Berita


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Berita).offset(skip).limit(limit).all()


def get_title(db: Session, title: str):
    return db.query(Berita).filter(Berita.title.contains(title.capitalize())).all()


def get_date(db: Session, date: str):
    return db.query(Berita).filter(Berita.date == date).all()


def get_category(db: Session, category: str):
    return db.query(Berita).filter(Berita.category == category).all()


def get_website(db: Session, website: str):
    return db.query(Berita).filter(Berita.website.contains(website)).all()


def get_author(db: Session, author: str):
    return db.query(Berita).filter(Berita.author.contains(author.capitalize())).all()
