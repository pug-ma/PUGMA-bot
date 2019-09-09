FROM python:3.7-slim-buster

# Diretório pro projeto
RUN useradd --create-home appuser
WORKDIR /home/appuser

# Install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Rode o container como usuário não-root
USER appuser

# Copia o projeto
COPY . .

# Rode o bot
CMD ["python", "app.py"]
