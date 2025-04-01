# Usa a imagem oficial do Python 3.12
FROM python:3.12

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY ../pyproject.toml ../poetry.lock ../streamlit_for_crag.py ../settings.py ../.env ./

# Instala o Poetry
RUN pip install --no-cache-dir poetry

# Instala as dependências sem criar um ambiente virtual dentro do contêiner
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "streamlit_for_crag.py", "--server.port=8501", "--server.address=0.0.0.0"]
