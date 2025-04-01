from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Carrega o .env
load_dotenv()

class Settings(BaseSettings):
    PORT: str
    HOST: str

    class Config:
        env_prefix = 'API_'  # Prefixo para as variáveis de ambiente
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()