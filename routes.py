from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
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

@router.get("/title/{title}")
async def filter_title(title:str,db:Session = Depends(get_db)):
    _berita = crud.get_title(db,title)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

@router.get("/date/{date}")
async def filter_date(date:str,db:Session = Depends(get_db)):
    _berita = crud.get_date(db,date)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

@router.get("/website/{website}")
async def filter_website(website:str,db:Session = Depends(get_db)):
    _berita = crud.get_website(db,website)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

@router.get("/category/{category}")
async def filter_category(category:str,db:Session = Depends(get_db)):
    _berita = crud.get_category(db,category)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)

@router.get("/author/{author}")
async def filter_author(author:str,db:Session = Depends(get_db)):
    _berita = crud.get_author(db,author)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_berita)



