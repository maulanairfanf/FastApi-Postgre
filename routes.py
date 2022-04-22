from unicodedata import category
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response
from typing import Optional
import crud
from pydantic import BaseModel

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
async def filter_title(title: str, db: Session = Depends(get_db), limit: Optional[int] = None):
    _berita = crud.get_title(db, title, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/date={date}")
async def filter_date(date: "str", db: Session = Depends(get_db), limit: Optional[int] = None):
    _berita = crud.get_date(db, date, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/website={website}")
async def filter_website(website: str, db: Session = Depends(get_db), limit: Optional[int] = None):
    _berita = crud.get_website(db, website, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/category={category}")
async def filter_category(category: str, db: Session = Depends(get_db), limit: Optional[int] = None):
    _berita = crud.get_category(db, category, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/author={author}")
async def filter_author(author: str, db: Session = Depends(get_db), limit: Optional[int] = None):
    _berita = crud.get_author(db, author, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)


@router.get("/more_params")
async def more_params(db: Session = Depends(get_db), title: Optional[str] = None, date: Optional[str] = None, website: Optional[str] = None, category: Optional[str] = None, author: Optional[str] = None, limit: Optional[int] = None):
    _berita = crud.more_params(
        db, title, date, website, category, author, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)
