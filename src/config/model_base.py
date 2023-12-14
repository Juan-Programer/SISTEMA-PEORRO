from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ModelBase():
    created_at = Column(DateTime, default=datetime.now(), nullable = False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable = False)
