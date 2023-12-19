from src.config.database import engine
from sqlalchemy.orm import sessionmaker

SessionDatabase = sessionmaker(bind=engine)
