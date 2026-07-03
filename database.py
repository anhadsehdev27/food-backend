from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Anhad%401458@localhost:5432/food"

SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_U2XKkqbDaPi6@ep-round-bar-at24x6zg.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

engine  = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autoflush= False, autocommit = False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def create_table():
    Base.metadata.create_all(bind = engine)