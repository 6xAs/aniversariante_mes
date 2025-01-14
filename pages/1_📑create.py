import streamlit as st 
import pandas as pd
import os
from PIL import Image
import requests
from io import BytesIO

### Configuração da página
st.set_page_config(
    page_title="Cadastrar Aniversariante",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Cadastro Aniversariante")
st.write("Preencha o formulário abaixo para cadastrar um aniversariante")

# Entrada de Texto 
nome = st.text_input("Nome")

# Botão de envio
if st.button("Cadastrar"):
    st.write(f"Olá, {nome}! Seu cadastro foi realizado com sucesso!")
else:
    st.write("Digite seu nome e pressione o botão para cadastrar")
    

# Dataframe Atores Aniversariantes
df = pd.read_csv('_datasets/atores_aniversariantes.csv' , sep=',', encoding='utf-8')

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

  # Ajuste o tamanho conforme necessário
