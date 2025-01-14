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

# Carregar balões de aniversário
st.balloons()

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

# Função para converter GIF para base64
def get_gif_base64(path):
    with open(path, "rb") as gif_file:
        return base64.b64encode(gif_file.read()).decode()

# Converter o GIF para base64
gif_right_base64 = get_gif_base64("assets/images/gifs/confete_Right.gif")
gif_left_base64 = get_gif_base64("assets/images/gifs/confete_Left.gif")
gif_background_base64 = get_gif_base64("assets/images/gifs/gif_background.gif")

# Estilo CSS para centralizar e arredondar a imagem e definir o plano de fundo
st.markdown(
    f"""
    <style>
    body {{
        background-image: url("data:image/gif;base64,{gif_background_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .center {{
        padding: 5px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-top: 5px;
        position: relative;
        z-index: 2;
    }}
    .round-img {{
        border-radius: 50%;
        width: 400px; /* Ajuste o tamanho da imagem */
        height: 400px;
        object-fit: cover; /* Garante que a imagem fique bem ajustada */
    }}
    .titles {{
        text-align: center;
        margin-top: 5px;
    }}
    .titles h3 {{
        margin: 5px;
    }}
    .titles h1 {{
        padding: 5px;
        color: #FFD700;
        font-size: 3em; /* Ajuste o tamanho do h1 se necessário */
    }}
    .titles h5 {{
        margin: 5px;
        color: gray; /* Ajuste a cor do h5 */
    }}
    .gif-center {{
        position: absolute;
        top: 120%;
        left: 50%;
        height: 100%;
        width: 100%;
        transform: translate(-50%, -50%);
        z-index: 1;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Exibir o GIF no centro da página, atrás da imagem principal
st.markdown(
    f"""
    <div class="gif-center">
        <img src="data:image/gif;base64,{gif_background_base64}" alt="Confete">
    </div>
    """,
    unsafe_allow_html=True
)

# Exibir a imagem e as informações no markdown
st.markdown(
    f"""
    <div class="center">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Imagem arredondada" class="round-img">
        <div class="titles">
            <h4> <span> <img src="data:image/gif;base64,{gif_left_base64}" alt="Confete"> </span> Parabéns<span> <img src="data:image/gif;base64,{gif_right_base64}" alt="Confete"> </span></h4>
            <h1>{name}</h1>
            <h5>{date_of_birth}</h5>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
