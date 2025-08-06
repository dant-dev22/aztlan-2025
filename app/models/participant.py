# app/models/participant.py
from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    experience = Column(String, nullable=False)
    belt_color = Column(String, nullable=False)
    club = Column(String, nullable=False)
    biological_sex = Column(String, nullable=False)