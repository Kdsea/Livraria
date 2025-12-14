from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. URL do banco (Para PostgreSQL seria: postgresql://user:senha@localhost/db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./loja.db"

# 2. Criar o motor (engine)
# check_same_thread=False é necessário apenas para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Criar a classe de Sessão (que usaremos para salvar/buscar dados)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Classe base para criar os modelos (tabelas)
Base = declarative_base()