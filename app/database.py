from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'mysql://biouser:1234qwer@127.0.0.7:3306/bioDB?charset=utf8mb4'

engine = create_engine(
    SQLALCHAMY_DATABASE_URL, 
    echo=True,
    pool_recycle=900, 
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()