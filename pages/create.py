import streamlit as st 
import os

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