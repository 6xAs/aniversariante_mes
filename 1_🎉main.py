import streamlit as st
import pandas as pd
import base64
import requests
from io import BytesIO
from PIL import Image
from datetime import datetime
import locale

# Tentar definir a localidade para português Brasil
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'pt_BR')

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

# Função para converter imagem para base64
def get_image_base64(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Função para converter GIF para base64
def get_gif_base64(path):
    with open(path, "rb") as gif_file:
        return base64.b64encode(gif_file.read()).decode()

# Converter os GIFs para base64
gif_right_base64 = get_gif_base64("assets/images/gifs/confete_Right.gif")
gif_left_base64 = get_gif_base64("assets/images/gifs/confete_Left.gif")
gif_background_base64 = get_gif_base64("assets/images/gifs/gif_background.gif")

# Estilo CSS para centralizar e arredondar a imagem e definir o plano de fundo
st.markdown(
    f"""
    <style>
    body {{
        background: none;
    }}
    .background-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .background-img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
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
        border: 10px solid #DAA520;
        border-radius: 150px;
        width: 800px;
        background-position: center;
        
        border-radius: 50%;
        width: 400px; 
        height: 400px;
        object-fit: cover; 
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
        color: #DAA520;
        font-size: 5em; 
    }}
    .titles h5 {{
        font-size: 2.5em; 
        margin: 5px;
        color: gray; 
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Exibir a imagem de fundo
st.markdown(
    f"""
    <div class="background-container">
        <img src="data:image/gif;base64,{gif_background_base64}" alt="Imagem de fundo" class="background-img">
    </div>
    """,
    unsafe_allow_html=True
)

# Função para verificar aniversariantes e exibir informações
def exibir_aniversariantes(df):
    hoje = datetime.today().strftime("%d-%m")
    aniversariantes = df[df['Date_of_Birth'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%d-%m") == hoje)]
    
    if not aniversariantes.empty:
        # Carregar balões de aniversário
        st.balloons()
        for _, record in aniversariantes.iterrows():
            name = record['Name']
            date_of_birth = datetime.strptime(record['Date_of_Birth'], "%Y-%m-%d").strftime("%d de %B")
            image_url = record['Image_URL']
            image_base64 = get_image_base64(image_url)
            
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
    else:
        st.markdown(
            """
            <div class="center">
                <div class="titles">
                    <h1>😢 Nenhum aniversariante hoje</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Chamar a função para exibir aniversariantes
exibir_aniversariantes(df)


