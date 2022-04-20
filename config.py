from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://lcwsaujkplbtoa:f222a0c158038fbc55d1b815143ab41e42f3ae27f9d8d999ef7c944e4490cda6@ec2-34-197-84-74.compute-1.amazonaws.com:5432/d93p694gn91dn4'
# DATABASE_URL = 'postgresql://postgres:TanpaPassword@localhost:5432/webScraping'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
