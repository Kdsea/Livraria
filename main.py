from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, SessionLocal

# Cria as tabelas no banco de dados automaticamente
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- Schemas (Validação de dados com Pydantic) ---
class ProdutoCreate(BaseModel):
    nome: str
    editora: str
    autor: str
    alugado: bool = False

class ProdutoResponse(ProdutoCreate):
    id: int
    class Config:
        from_attributes = True # Permite ler dados do ORM

# --- Dependência (Injeção de Dependência) ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # Fecha a conexão sempre!

# --- Rotas ---

@app.post("/produtos/", response_model=ProdutoResponse)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    # Cria o objeto do banco (Model) usando os dados validados (Schema)
    novo_produto = models.ProdutoDB(**produto.dict())
    
    db.add(novo_produto)  # Adiciona na "fila"
    db.commit()           # Salva efetivamente no banco
    db.refresh(novo_produto) # Recarrega com o ID gerado pelo banco
    return novo_produto

@app.get("/produtos/", response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    # Busca todos os registros da tabela
    return db.query(models.ProdutoDB).all()