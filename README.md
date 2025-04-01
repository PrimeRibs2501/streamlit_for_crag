# Streamlit for CRAG (EM DESENVOLVIMENTO)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## Sobre o Projeto

O **Streamlit for CRAG** é uma aplicação web interativa desenvolvida com Streamlit para facilitar fluxos de trabalho relacionados ao CRAG (Custom Resource Allocation Generator). A aplicação é escalável e utiliza Docker para implantação.

---

## Tecnologias Principais

- **Python**: Linguagem base do projeto
- **Streamlit**: Framework para criação de aplicações web interativas
- **Docker**: Containerização da aplicação

---

## Requisitos

- Python 3.8+
- Docker e Docker Compose

---

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/PrimeRibs2501/streamlit_for_crag.git
   cd streamlit_for_crag
   ```

2. Instale as dependências utilizando Poetry:
   ```
   poetry install
   ```

3. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto.
   - Adicione as configurações necessárias (consulte `settings.py`).

4. Execute a aplicação:
   ```
   streamlit run streamlit_for_crag.py
   ```

---

## Uso

### Localmente

1. Após executar o comando acima, acesse a aplicação em `http://localhost:8501`.
2. Utilize a interface para interagir com as ferramentas relacionadas ao CRAG.

### Com Docker

1. Construa a imagem Docker:
   ```
   docker build -t streamlit_for_crag .
   ```

2. Execute o container:
   ```
   docker run -p 8501:8501 streamlit_for_crag
   ```

---

## Estrutura do Projeto

```
streamlit_for_crag/
├── docker/               # Arquivos relacionados ao Docker
├── .env                  # Variáveis de ambiente
├── .gitignore            # Regras de exclusão do Git
├── poetry.lock           # Arquivo de bloqueio de dependências (Poetry)
├── pyproject.toml        # Configuração do projeto (Poetry)
├── settings.py           # Configurações da aplicação
├── streamlit_for_crag.py # Script principal da aplicação Streamlit
```

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`).
3. Commit suas alterações (`git commit -m 'Add some AmazingFeature'`).
4. Push para a branch (`git push origin feature/AmazingFeature`).
5. Abra um Pull Request.
