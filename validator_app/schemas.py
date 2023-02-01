from pydantic import BaseModel


class DocumentBase(BaseModel):
    number: str
    doc_type: str


class DocumentCreate(DocumentBase):
    pass


class Document(DocumentBase):
    id: int
    blocked: bool

    class Config:
        orm_mode = True
