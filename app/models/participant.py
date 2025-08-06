from pydantic import BaseModel
from datetime import date

class Participant(BaseModel):
    name: str
    birth_date: date
    training_duration: str
    belt_color: str
    club: str
    biological_sex: str