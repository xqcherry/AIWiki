from sqlalchemy.orm import Session

from src.model.model import Document

class DocusMapper:
    def __init__(self, db: Session):
        self.db = db

    def create(self, doc: Document):
        self.db.add(doc)
        self.db.commit()
        self.db.refresh(doc)
        return doc

    def update(self, doc: Document):
        self.db.commit()
        self.db.refresh(doc)
        return doc

    def delete(self, doc: Document):
        self.db.delete(doc)
        self.db.commit()

    def get_all_id(self, skip: int = 0, limit: int = 100):
        return self.db.query(Document).offset(skip).limit(limit).all()

    def get_by_id(self, document_id: int):
        return self.db.query(Document).filter(Document.id == document_id).first()

    def count(self):
        return self.db.query(Document).count()