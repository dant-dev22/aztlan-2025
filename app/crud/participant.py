import random
from sqlalchemy.orm import Session
from app.models.participant import Participant
from app.schemas.participant import ParticipantBase

def generate_unique_aztlan_id(db: Session):
    while True:
        random_number = random.randint(100000, 999999)
        aztlan_id = f"aztlan-{random_number}"
        existing = db.query(Participant).filter_by(aztlan_id=aztlan_id).first()
        if not existing:
            return aztlan_id

def get_all_participants(db: Session):
    return db.query(Participant).all()

def create_participant(db: Session, participant_data: ParticipantBase):
    aztlan_id = generate_unique_aztlan_id(db)
    db_participant = Participant(**participant_data.dict(), aztlan_id=aztlan_id)
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant