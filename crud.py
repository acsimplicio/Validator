from sqlalchemy.orm import Session

from . import models, schemas

def get_document(db: Session, document_id: int):
    return db.query(models.Document).filter(models.Document.id == document_id).first()

def get_document_by_number(db: Session, number: str):
    return db.query(models.Document).filter(models.Document.number == number).first()

def get_documents(db: Session):
    return db.query(models.Document).all()

def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(number=document.number, doc_type=document.doc_type)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document
