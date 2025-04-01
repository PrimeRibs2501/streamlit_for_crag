import streamlit as st
import requests
import os
from settings import settings

url = f'{settings.HOST}'#:{settings.PORT}'

# Sidebar para navegação
st.sidebar.title("Navegação")
option = st.sidebar.radio("Escolha uma opção:", [
    "Adicionar Documentos na API",
    "Listar coleções",
    "Listar documentos",
    "Deletar documentos"
])

if option == "Adicionar Documentos na API":
    st.title("Adicionar Documentos na API")

    uploaded_file = st.file_uploader("Faça upload de um arquivo", type=["pdf"])

    # Campos para entrada de dados
    tags_documents = st.text_input("Tags dos documentos (opicional)")
    ids = st.text_input("IDs (opcional)")

    # Monta o payload
    payload = {}
    if ids:
        payload["ids"] = ids
    if tags_documents:
        payload["tags"] = tags_documents

    # Botão para enviar a requisição
    if st.button("Adicionar Documento"):
        if uploaded_file:
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            response = requests.put(f"{url}/files/upload", files=files)
            if response.status_code == 201:
                st.success("Documento adicionado com sucesso!")
            else:
                st.error(f"Erro ao adicionar documento: {response.text}")
        else:
            st.warning("Faça o upload de um arquivo.")

elif option == "Listar documentos":
    st.title("Listar Documentos")
    collection_name = st.text_input("Nome da coleção")
 
    if st.button("Listar"):
        response = requests.get(f"{url}/files/list_files/{collection_name}")
        if response.status_code == 200:
            response = response.json().get("response", {})
            data = response.get("files", {})
            ids = data.get("ids", [])
            documents = data.get("documents", [])

            # Junta os ids com os documentos
            for i in range(len(ids)):
                doc_id = ids[i]
                content = documents[i]
                preview = '\n'.join(content.splitlines()[:2])
                st.write(f"**ID:** {doc_id}")
                st.text_area("Prévia do Documento", preview, height=100, disabled=True, key=f"preview_{doc_id}")
                st.write("---")
        else:
            st.error(f"Erro ao listar documentos: {response.text}")

elif option == "Listar coleções":
    st.title("Listar Coleções")
    response = requests.get(f"{url}/files/list_collections")
    
    if response.status_code == 200:
        collections = response.json().get("response", {}).get("collections", [])
        if collections:
            st.write("Coleções disponíveis:")
            for collection in collections:
                st.write(f"- {collection}")
        else:
            st.write("Nenhuma coleção encontrada.")
    else:
        st.error(f"Erro ao listar coleções: {response.text}")


elif option == "Deletar documentos":
    st.title("Deletar documentos")
    doc_id = st.text_input("ID do documento a deletar")
    collection_name = st.text_input("Nome da coleção o documento a deletar")

    if st.button("Deletar"):
        response = requests.delete(f"{url}/files/delete_file/{collection_name}/{doc_id}")
        if response.status_code == 204:
            st.success("Documento deletado com sucesso!")
        else:
            st.error(f"Erro ao deletar documento: {response.text}")