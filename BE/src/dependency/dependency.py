from fastapi import Depends
from sqlalchemy.orm import Session
from src.core.db import get_db
from src.services.services import DocusServices


def get_docus_services(db: Session = Depends(get_db)):
    return DocusServices(db)