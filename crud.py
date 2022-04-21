from sqlalchemy.orm import Session
from models import Berita


def query_title(table, column):
    return table.title.contains(column.capitalize())


def query_author(table, column):
    return table.author.contains(column.capitalize())


def query_date(table, column):
    return table.date == column


def query_website(table, column):
    return table.website.contains(column.lower())


def query_category(table, column):
    return table.category.contains(column.lower())


# single query


def get_all(db: Session):
    return db.query(Berita).all()


def get_title(db: Session, title: str):
    return db.query(Berita).filter(query_title(Berita, title)).all()


def get_date(db: Session, date: str):
    return db.query(Berita).filter(query_date(Berita, date)).all()


def get_category(db: Session, category: str):
    return db.query(Berita).filter(query_category(Berita, category)).all()


def get_website(db: Session, website: str):
    return db.query(Berita).filter(query_website(Berita, website)).all()


def get_author(db: Session, author: str):
    return db.query(Berita).filter(query_author(Berita, author)).all()

# 2 query title


def get_title_date(db: Session, title: str, date: str):
    return db.query(Berita).filter(query_title(Berita, title), query_date(Berita, date)).all()


def get_title_website(db: Session, title: str, website: str):
    return db.query(Berita).filter(query_title(Berita, title), query_website(Berita, website)).all()


def get_title_category(db: Session, title: str, category: str):
    return db.query(Berita).filter(query_title(Berita, title), query_category(Berita, category)).all()


def get_title_author(db: Session, title: str, author: str):
    return db.query(Berita).filter(query_title(Berita, title), query_author(Berita, author)).all()

# 2 query date


def get_date_website(db: Session, date: str, website: str):
    return db.query(Berita).filter(query_date(Berita, date), query_website(Berita, website)).all()


def get_date_category(db: Session, date: str, category: str):
    return db.query(Berita).filter(query_date(Berita, date), query_category(Berita, category)).all()


def get_date_author(db: Session, date: str, author: str):
    return db.query(Berita).filter(query_date(Berita, date), query_author(Berita, author)).all()

# 2 query website


def get_website_category(db: Session, website: str, category: str):
    return db.query(Berita).filter(query_website(Berita, website), query_category(Berita, category)).all()


def get_website_author(db: Session, website: str, author: str):
    return db.query(Berita).filter(query_website(Berita, website), query_author(Berita, author)).all()

# 2 query category


def get_category_author(db: Session, category: str, author: str):
    return db.query(Berita).filter(query_category(Berita, category), query_author(Berita, author)).all()

# single limit


def get_all_limit(db: Session, limit: int):
    return db.query(Berita).limit(limit).all()


def get_title_limit(db: Session, title: str, limit: int):
    return db.query(Berita).filter(query_title(Berita, title)).limit(limit).all()


def get_date_limit(db: Session, date: str, limit: int):
    return db.query(Berita).filter(query_date(Berita, date)).limit(limit).all()


def get_website_limit(db: Session, website: str, limit: int):
    return db.query(Berita).filter(query_website(Berita, website)).limit(limit).all()


def get_category_limit(db: Session, category: str, limit: int):
    return db.query(Berita).filter(query_category(Berita, category)).limit(limit).all()


def get_author_limit(db: Session, author: str, limit: int):
    return db.query(Berita).filter(query_author(Berita, author)).limit(limit).all()

# 2 query title limit


def get_title_date_limit(db: Session, title: str, date: str, limit: int):
    return db.query(Berita).filter(query_title(Berita, title), query_date(Berita, date)).limit(limit).all()


def get_title_website_limit(db: Session, title: str, website: str, limit: int):
    return db.query(Berita).filter(query_title(Berita, title), query_website(Berita, website)).limit(limit).all()


def get_title_category_limit(db: Session, title: str, category: str, limit: int):
    return db.query(Berita).filter(query_title(Berita, title), query_category(Berita, category)).limit(limit).all()


def get_title_author_limit(db: Session, title: str, author: str, limit: int):
    return db.query(Berita).filter(query_title(Berita, title), query_author(Berita, author)).limit(limit).all()

# 2 query date limit


def get_date_website_limit(db: Session, date: str, website: str, limit: int):
    return db.query(Berita).filter(query_date(Berita, date), query_website(Berita, website)).limit(limit).all()


def get_date_category_limit(db: Session, date: str, category: str, limit: int):
    return db.query(Berita).filter(query_date(Berita, date), query_category(Berita, category)).limit(limit).all()


def get_date_author_limit(db: Session, date: str, author: str, limit: int):
    return db.query(Berita).filter(query_date(Berita, date), query_author(Berita, author)).limit(limit).all()

# 2 query website limit


def get_website_category_limit(db: Session, website: str, category: str, limit: int):
    return db.query(Berita).filter(query_website(Berita, website), query_category(Berita, category)).limit(limit).all()


def get_website_author_limit(db: Session, website: str, author: str, limit: int):
    return db.query(Berita).filter(query_website(Berita, website), query_author(Berita, author)).limit(limit).all()

# 2 query category limit


def get_category_author_limit(db: Session, category: str, author: str, limit: int):
    return db.query(Berita).filter(query_category(Berita, category), query_author(Berita, author)).limit(limit).all()
