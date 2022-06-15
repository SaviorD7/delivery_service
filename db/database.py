# Import objects
from importlib.metadata import metadata
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from contextlib import closing
import socket

# Settings as shown in docker-compose.yml

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@db/info'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Session = sessionmaker(bind=engine)
Base = declarative_base()