from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# mysql+pymysql//u116665791_maulanairfanf:TanpaPassword79@sql596.main-hosting.eu/u116665791_WebScraping

DATABASE_URL = 'mysql+pymysql://u116665791_maulanairfanf:TanpaPassword79@31.220.110.101:3306/u116665791_WebScraping'
# DATABASE_URL = 'postgresql://postgres:TanpaPassword@localhost:5432/webScraping'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
