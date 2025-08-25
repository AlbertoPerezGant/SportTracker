from sqlalchemy import create_engine, Column, Integer, Float, String, Date, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f"sqlite:///data/workouts.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    csv_id = Column(Integer, unique=True, index=True)
    date = Column(Date)
    duration_min = Column(Float)
    distance_km = Column(Float)
    avg_hr = Column(Integer)
    max_hr = Column(Integer)
    calories = Column(Integer)
    __table_args__ = (UniqueConstraint('csv_id', name='uix_csv_id'),)

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)