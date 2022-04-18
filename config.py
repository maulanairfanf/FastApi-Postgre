from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://vrsvsluhxmvrnh:1be4aa85913309c31a26df4842d9763f7dd4dca289aad373fea555a3542d499f@ec2-34-192-210-139.compute-1.amazonaws.com:5432/deqif9hrnf9p2t'
# DATABASE_URL = 'postgresql://postgres:TanpaPassword@localhost:5000/webScraping'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
