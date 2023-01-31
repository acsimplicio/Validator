from sqlalchemy import Boolean, CheckConstraint, Column, Integer, String 

from .database import Base

class Document(Base):
    __tablename__ = "document"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, index=True, unique=True)
    doc_type = Column(String)
    blocked = Column(Boolean, default=False)
    __table_args__ = (CheckConstraint(doc_type.in_(["CPF", "CNPJ"])))
