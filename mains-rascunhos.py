import streamlit as st
import pandas as pd
import base64
import requests
from io import BytesIO
from PIL import Image
from datetime import datetime


### Configuração da página
st.set_page_config(
    page_title="Teste Imagem Arredondada",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Carregar o DataFrame
df = pd.read_csv('_datasets/atores_aniversariantes.csv', sep=',', encoding='utf-8')

# Remover linhas vazias
df = df.dropna(how='all')

# Selecionar o primeiro registro (ou qualquer outro critério)
record = df.iloc[0]

# Extrair informações
name = record['Name']
date_of_birth = record['Date_of_Birth']
image_url = record['Image_URL']

# Converter a data para o formato desejado
date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").strftime("%d de %B de %Y")

# Função para converter imagem para base64
def get_image_base64(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Converter a imagem para base64
image_base64 = get_image_base64(image_url)

# Estilo CSS para centralizar e arredondar a imagem
st.markdown(
    """
    <style>
    .center {
        padding: 5px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-top: 5px;
    }
    .round-img {
        border-radius: 50%;
        width: 400px; /* Ajuste o tamanho da imagem */
        height: 400px;
        object-fit: cover; /* Garante que a imagem fique bem ajustada */
    }
    .titles {
        text-align: center;
        margin-top: 5px;
    }
    .titles h3 {
        margin: 5px;
    }
    .titles h1 {
        padding: 5px;
        color: #FFD700;
        font-size: 3em; /* Ajuste o tamanho do h1 se necessário */
    }
    .titles h5 {
        margin: 5px;
        color: gray; /* Ajuste a cor do h5 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Exibir a imagem e as informações no markdown
st.markdown(
    f"""
    <div class="center">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Imagem arredondada" class="round-img">
        <div class="titles">
            <h4>🎉🎈Parabéns🎈🎉</h4>
            <h1>{name}</h1>
            <h5>{date_of_birth}</h5>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


import streamlit as st
import pandas as pd
import base64
import requests
from io import BytesIO
from PIL import Image
from datetime import datetime
import locale

# Definir a localidade para português Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

### Configuração da página
st.set_page_config(
    page_title="Teste Imagem Arredondada",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Carregar o DataFrame
df = pd.read_csv('_datasets/atores_aniversariantes.csv', sep=',', encoding='utf-8')

# Remover linhas vazias
df = df.dropna(how='all')

# Selecionar o primeiro registro (ou qualquer outro critério)
record = df.iloc[0]

# Extrair informações
name = record['Name']
date_of_birth = record['Date_of_Birth']
image_url = record['Image_URL']

# Converter a data para o formato desejado (dia e mês em português)
date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").strftime("%d de %B")

# Função para converter imagem para base64
def get_image_base64(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Converter a imagem para base64
image_base64 = get_image_base64(image_url)

# Estilo CSS para centralizar e arredondar a imagem
st.markdown(
    """
    <style>
    .center {
        padding: 5px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-top: 5px;
    }
    .round-img {
        border-radius: 50%;
        width: 400px; /* Ajuste o tamanho da imagem */
        height: 400px;
        object-fit: cover; /* Garante que a imagem fique bem ajustada */
    }
    .titles {
        text-align: center;
        margin-top: 5px;
    }
    .titles h3 {
        margin: 5px;
    }
    .titles h1 {
        padding: 5px;
        color: #FFD700;
        font-size: 3em; /* Ajuste o tamanho do h1 se necessário */
    }
    .titles h5 {
        margin: 5px;
        color: gray; /* Ajuste a cor do h5 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Exibir a imagem e as informações no markdown
st.markdown(
    f"""
    <div class="center">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Imagem arredondada" class="round-img">
        <div class="titles">
            <h4>🎉🎈Parabéns🎈🎉</h4>
            <h1>{name}</h1>
            <h5>{date_of_birth}</h5>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
