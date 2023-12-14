from sqlalchemy import create_engine

database_string: str = f"sqlite:///app.db"
engine = create_engine(database_string, echo = True)