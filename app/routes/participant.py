from fastapi import APIRouter
from app.models.participant import Participant

router = APIRouter(prefix="/participants")

@router.get("", response_model=list[Participant])
def get_participants():
    return [
        {
            "name": "Jane Doe",
            "birth_date": "2000-01-01",
            "experience": "3 years",
            "belt_color": "blue",
            "club": "Warriors",
            "biological_sex": "female"
        }
    ]

@router.post("")
def create_participant(participant: Participant):
    print("New participant received:")
    print(participant)
    return {"message": "Participant received successfully"}