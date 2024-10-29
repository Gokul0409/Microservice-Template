from app.utils.toml_parser import read_toml
from sqlalchemy import create_engine
from app.model.user_model import Base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

""" 
This is Configuration file of service.

 - Sqlalchemy engine is initialized using db toml.

"""

DB_TOML = Path("app/config/db.toml")

db_config = read_toml(toml_path=DB_TOML)

engine = create_engine(db_config.database.DB_URL)

Session = sessionmaker(bind=engine, autoflush=False)

def initialize_db():
    Base.metadata.create_all(engine)