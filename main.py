from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/documents/", response_model=schemas.Document)
def create_document(document: schemas.DocumentCreate, db: Session = Depends(get_db)):
    db_document = crud.get_document_by_number(db, number=document.number)
    if db_document:
        raise HTTPException(status_code=400, detail="Número de documento já cadastrado")
    return crud.create_document(db=db, document=document)

@app.get("/documents/", response_model=list[schemas.Document])
def read_documents(db: Session = Depends(get_db)):
    documents = crud.get_documents(db=db)
    return documents
