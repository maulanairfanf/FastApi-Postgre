from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://sgipiulsrqjqyd:c03109765d8a9574c3adc9273c6e07f531997fbfe0722e1c40e93d8184b0b53f@ec2-34-231-63-30.compute-1.amazonaws.com:5432/durspbi4nbo1m'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()