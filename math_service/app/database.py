
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./operations.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class OperationLog(Base):
    __tablename__ = "operations"
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String)
    input = Column(String)
    output = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
