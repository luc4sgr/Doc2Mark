# Imagem base leve com Python
FROM python:3.12-slim

# Diretório onde a aplicação será executada
WORKDIR /app

# Copiar tudo (inclusive src/ e run.py)
COPY . .

# Instalar dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expor a porta onde o Flask está rodando
EXPOSE 3000

# Comando para iniciar a aplicação
CMD ["python", "run.py"]
