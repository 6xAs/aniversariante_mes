import streamlit as st 
import pandas as pd
import os
from PIL import Image
import requests
from io import BytesIO
from datetime import datetime

### Configuração da página
st.set_page_config(
    page_title="Cadastrar Aniversariante",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Cadastro Aniversariante")
st.write("Preencha o formulário abaixo para cadastrar um aniversariante")

# Formulario dos aniversariantes
aniversariante = st.form("aniversariante")
with aniversariante:
    nome = st.text_input("Nome")
    data_nascimento = st.date_input("Data de Nascimento", value=datetime.today(), format="DD/MM/YYYY")
    foto = st.file_uploader("Foto")
    submit_button = st.form_submit_button(label="Cadastrar")

    if submit_button:
        data_nascimento_formatada = data_nascimento.strftime("%d/%m/%Y")
        st.write(f"Aniversariante {nome} cadastrado com sucesso! Data de Nascimento: {data_nascimento_formatada}")

# Dataframe Atores Aniversariantes
df = pd.read_csv('_datasets/atores_aniversariantes.csv', sep=',', encoding='utf-8')

# Remover linhas vazias
df = df.dropna(how='all')

columns = ["Name", "Date_of_Birth", "Image_URL"]

# Exibir DataFrame
st.dataframe(df[columns],
             column_config={
                    "Name": {"max_width": 100},
                    # Formato de data 
                    "Date_of_Birth": st.column_config.DateColumn(format="DD/MM/YYYY"),
                    "Image_URL": st.column_config.ImageColumn("Image_URL", width=200),
             }, height=300, width=800)  # Ajuste a altura e a largura conforme necessário
