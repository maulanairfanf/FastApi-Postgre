from fastapi import APIRouter, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response
import crud

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def get_all(db: Session = Depends(get_db)):
    _berita = crud.get_all(db)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

# single params


@router.get("/title={title}")
async def filter_title(title: str, db: Session = Depends(get_db)):
    _berita = crud.get_title(db, title)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/date={date}")
async def filter_date(date: str, db: Session = Depends(get_db)):
    _berita = crud.get_date(db, date)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/website={website}")
async def filter_website(website: str, db: Session = Depends(get_db)):
    _berita = crud.get_website(db, website)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/category={category}")
async def filter_category(category: str, db: Session = Depends(get_db)):
    _berita = crud.get_category(db, category)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/author={author}")
async def filter_author(author: str, db: Session = Depends(get_db)):
    _berita = crud.get_author(db, author)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

# params 2 title


@router.get("/title={title}/date={date}")
async def filter_title_date(title: str, date: str, db: Session = Depends(get_db)):
    _berita = crud.get_title_date(db, title, date)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/title={title}/website={website}")
async def filter_title_website(title: str, website: str, db: Session = Depends(get_db)):
    _berita = crud.get_title_website(db, title, website)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/title={title}/category={category}")
async def filter_title_category(title: str, category: str, db: Session = Depends(get_db)):
    _berita = crud.get_title_category(db, title, category)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/title={title}/author={author}")
async def filter_title_author(title: str, author: str, db: Session = Depends(get_db)):
    _berita = crud.get_title_author(db, title, author)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

# params 2 date


@router.get("/date={date}/website={website}")
async def filter_date_date(date: str, website: str, db: Session = Depends(get_db)):
    _berita = crud.get_date_website(db, date, website)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/date={date}/category={category}")
async def filter_date_category(date: str, category: str, db: Session = Depends(get_db)):
    _berita = crud.get_date_category(db, date, category)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/date={date}/author={author}")
async def filter_date_author(date: str, author: str, db: Session = Depends(get_db)):
    _berita = crud.get_date_author(db, date, author)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

# params 2 website


@router.get("/website={website}/category={category}")
async def filter_website_category(website: str, category: str, db: Session = Depends(get_db)):
    _berita = crud.get_website_category(db, website, category)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/website={website}/author={author}")
async def filter_website_author(website: str, author: str, db: Session = Depends(get_db)):
    _berita = crud.get_website_author(db, website, author)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

# params 2 category

@router.get("/category={category}/author={author}")
async def filter_category_author(category: str, author: str, db: Session = Depends(get_db)):
    _berita = crud.get_category_author(db, category, author)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

# single limit


@router.get("/limit={limit}")
async def get_all_limit(limit: int, db: Session = Depends(get_db)):
    _berita = crud.get_all_limit(db, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/title={title}/limit={limit}")
async def filter_title_limit(title: str, limit: int, db: Session = Depends(get_db)):
    _berita = crud.get_title_limit(db, title, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/date={date}/limit={limit}")
async def filter_date_limit(date: str, limit: int, db: Session = Depends(get_db)):
    _berita = crud.get_date_limit(db, date, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/website={website}/limit={limit}")
async def filter_website_limit(website: str, limit: int, db: Session = Depends(get_db)):
    _berita = crud.get_website_limit(db, website, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/category={category}/limit={limit}")
async def filter_category_limit(category: str, limit: int, db: Session = Depends(get_db)):
    _berita = crud.get_category_limit(db, category, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/author={author}/limit={limit}")
async def filter_author_limit(author: str, limit: int, db: Session = Depends(get_db)):
    _berita = crud.get_author_limit(db, author, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

# 2 params title limit


@router.get("/title={title}/date={date}/limit={limit}")
async def filter_title_date_limit(title: str, date: str, limit=int, db: Session = Depends(get_db)):
    _berita = crud.get_title_date_limit(db, title, date, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/title={title}/website={website}/limit={limit}")
async def filter_title_website_limit(title: str, website: str, limit=int, db: Session = Depends(get_db)):
    _berita = crud.get_title_website_limit(db, title, website, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/title={title}/category={category}/limit={limit}")
async def filter_title_category_limit(title: str, category: str, limit=int, db: Session = Depends(get_db)):
    _berita = crud.get_title_category_limit(db, title, category, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/title={title}/author={author}/limit={limit}")
async def filter_title_author_limit(title: str, author: str, limit=int, db: Session = Depends(get_db)):
    _berita = crud.get_title_author_limit(db, title, author, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

# 2 params date limit


@router.get("/date={date}/website={website}/limit={limit}")
async def filter_date_website_limit(date: str, website: str, limit=int, db: Session = Depends(get_db)):
    _berita = crud.get_date_website_limit(db, date, website, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/date={date}/category={category}/limit={limit}")
async def filter_date_category_limit(date: str, category: str, limit=int, db: Session = Depends(get_db)):
    _berita = crud.get_date_category_limit(db, date, category, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/date={date}/author={author}/limit={limit}")
async def filter_date_author_limit(date: str, author: str, limit=int, db: Session = Depends(get_db)):
    _berita = crud.get_date_author_limit(db, date, author, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

# 2 params website limit


@router.get("/website={website}/category={category}/limit={limit}")
async def filter_website_category_limit(website: str, category: str, limit=int, db: Session = Depends(get_db)):
    _berita = crud.get_website_category_limit(db, website, category, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/website={website}/author={author}/limit={limit}")
async def filter_website_author_limit(website: str, author: str, limit=int, db: Session = Depends(get_db)):
    _berita = crud.get_website_author_limit(db, website, author, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

# 2 parasm category limit


@router.get("/category={category}/author={author}/limit={limit}")
async def filter_category_author_limit(category: str, author: str, limit=int, db: Session = Depends(get_db)):
    _berita = crud.get_category_author_limit(db, category, author, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)
