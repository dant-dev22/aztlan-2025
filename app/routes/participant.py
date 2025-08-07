from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.participant import ParticipantBase, ParticipantOut
from app.database import get_db  # función que devuelve la sesión de DB
from app.crud import participant as crud_participant

router = APIRouter(prefix="/participants")

@router.get("", response_model=List[ParticipantOut])
def get_participants(db: Session = Depends(get_db)):
    return crud_participant.get_all_participants(db)

@router.post("", response_model=ParticipantOut)
def create_participant(participant: ParticipantBase, db: Session = Depends(get_db)):
    return crud_participant.create_participant(db, participant)
