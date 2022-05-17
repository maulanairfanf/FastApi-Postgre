from sqlalchemy.orm import Session
from models import Berita


def merge_query(table, column, params):
    if(params == "title"):
        return table.title.contains(column.capitalize())
    if(params == "author"):
        return table.author.contains(column.capitalize())
    if(params == "website"):
        return table.website.contains(column.lower())
    if(params == "date"):
        return table.date == column
    if(params == "category"):
        return table.category.contains(column.lower())


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


# Single Params
def get_all(db: Session, limit: int):
    if(limit is None):
        return db.query(Berita).all()
    else:
        return db.query(Berita).limit(limit).all()


def get_title(db: Session, title: str, limit: int):
    if(limit is None):
        return db.query(Berita).filter(query_title(Berita, title)).all()
    else:
        return db.query(Berita).filter(query_title(Berita, title)).limit(limit).all()


def get_date(db: Session, date: str, limit: int):
    if(limit is None):
        return db.query(Berita).filter(query_date(Berita, date)).all()
    else:
        return db.query(Berita).filter(query_date(Berita, date)).limit(limit).all()


def get_category(db: Session, category: str, limit: int):
    if(limit is None):
        return db.query(Berita).filter(query_category(Berita, category)).all()
    else:
        return db.query(Berita).filter(query_category(Berita, category)).limit(limit).all()


def get_website(db: Session, website: str, limit: int):
    if(limit is None):
        return db.query(Berita).filter(query_website(Berita, website)).all()
    else:
        return db.query(Berita).filter(query_website(Berita, website)).limit(limit).all()


def get_author(db: Session, author: str, limit: int):
    if(limit is None):
        return db.query(Berita).filter(query_author(Berita, author)).all()
    else:
        return db.query(Berita).filter(query_author(Berita, author)).limit(limit).all()


# More Params
def more_params(db: Session, title: str, date: str, website: str, category: str, author: str, limit=int):
    _count = 0
    arr_params = []
    arr_data_params = []
    if title is not None:
        arr_params.append("title")
        arr_data_params.append(title)
        _count = _count + 1

    if date is not None:
        arr_params.append("date")
        arr_data_params.append(date)
        _count = _count + 1

    if website is not None:
        arr_params.append("website")
        arr_data_params.append(website)
        _count = _count + 1

    if category is not None:
        arr_params.append("category")
        arr_data_params.append(category)
        _count = _count + 1

    if author is not None:
        arr_params.append("author")
        arr_data_params.append(author)
        _count = _count + 1

    if(limit is None):
        if(_count == 2):
            return db.query(Berita).filter(merge_query(Berita, arr_data_params[0], arr_params[0]), merge_query(Berita, arr_data_params[1], arr_params[1])).all()

        if(_count == 3):
            return db.query(Berita).filter(merge_query(Berita, arr_data_params[0], arr_params[0]), merge_query(Berita, arr_data_params[1], arr_params[1]), merge_query(Berita, arr_data_params[2], arr_params[2])).all()

        if(_count == 4):
            return db.query(Berita).filter(merge_query(Berita, arr_data_params[0], arr_params[0]), merge_query(Berita, arr_data_params[1], arr_params[1]), merge_query(Berita, arr_data_params[2], arr_params[2]), merge_query(Berita, arr_data_params[3], arr_params[3])).all()

        if(_count == 5):
            return db.query(Berita).filter(merge_query(Berita, arr_data_params[0], arr_params[0]), merge_query(Berita, arr_data_params[1], arr_params[1]), merge_query(Berita, arr_data_params[2], arr_params[2]), merge_query(Berita, arr_data_params[3], arr_params[3]), merge_query(Berita, arr_data_params[4], arr_params[4])).all()
    else:
        if(_count == 2):
            return db.query(Berita).filter(merge_query(Berita, arr_data_params[0], arr_params[0]), merge_query(Berita, arr_data_params[1], arr_params[1])).limit(limit).all()

        if(_count == 3):
            return db.query(Berita).filter(merge_query(Berita, arr_data_params[0], arr_params[0]), merge_query(Berita, arr_data_params[1], arr_params[1]), merge_query(Berita, arr_data_params[2], arr_params[2])).limit(limit).all()

        if(_count == 4):
            return db.query(Berita).filter(merge_query(Berita, arr_data_params[0], arr_params[0]), merge_query(Berita, arr_data_params[1], arr_params[1]), merge_query(Berita, arr_data_params[2], arr_params[2]), merge_query(Berita, arr_data_params[3], arr_params[3])).limit(limit).all()

        if(_count == 5):
            return db.query(Berita).filter(merge_query(Berita, arr_data_params[0], arr_params[0]), merge_query(Berita, arr_data_params[1], arr_params[1]), merge_query(Berita, arr_data_params[2], arr_params[2]), merge_query(Berita, arr_data_params[3], arr_params[3]), merge_query(Berita, arr_data_params[4], arr_params[4])).limit(limit).all()
