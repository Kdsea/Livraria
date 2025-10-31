FROM python:3.9-slim

LABEL authors="akaua"

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo da aplicação para o diretório de trabalho
COPY Livraria.py .

# Comando para executar a aplicação quando o contêiner iniciar
CMD ["python", "-u", "Livraria.py"]