from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class ProdutoDB(Base):
    __tablename__ = "Livros" # Nome da tabela no banco

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    autor = Column(String)
    editora = Column(String)
    alugado = Column(Boolean, default=False)