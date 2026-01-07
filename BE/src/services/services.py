from sqlalchemy.orm import Session

from src.mapper.mapper import DocusMapper
from src.schemas.schemas import DocusCreate, DocusUpdate
from src.model.model import Document


class DocusServices:
    def __init__(self, db: Session):
        self.mapper = DocusMapper(db)

    def create_document(self, data: DocusCreate):
        docs = Document(
            title=data.title,
            content=data.content,
        )
        return self.mapper.create(docs)

    def get_document(self, document_id):
        return self.mapper.get_by_id(document_id)

    def get_all_document(self, skip: int = 0, limit: int = 100):
        return self.mapper.get_all_id(skip, limit)

    def update_document(self, document_id: int, data: DocusUpdate):
        docs = self.mapper.get_by_id(document_id)

        if not docs:
            return None
        if data.title is not None:
            docs.title = data.title
        if data.content is not None:
            docs.content = data.content

        return self.mapper.update(docs)

    def delete_document(self, document_id: int):
        docs = self.mapper.get_by_id(document_id)

        if not docs:
            return None

        self.mapper.delete(docs)
        return True
