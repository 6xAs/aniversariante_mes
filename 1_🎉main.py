import streamlit as st
import pandas as pd
import os
import base64
import time
import streamlit.components.v1 as components


### Configuração da página
st.set_page_config(
    page_title="Teste Imagem Arredondada",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# Carrega o st.balloons apenas na página main.py quando a página for carregada
if 'st_balloons' not in st.session_state:
    # repete essa sessão a cada 10 segundos
    query_params = st.query_params
    page = query_params.get("page", ["1_🎉main"])[0]  # Página padrão é "1_🎉main"

    # Verifica se está na página '1_🎉main' e aplica o meta-refresh
    if page == "1_🎉main":
        st.markdown(
            """
            <meta http-equiv="refresh" content="100">
            """,
            unsafe_allow_html=True
        )
    st.session_state.st_balloons = st.balloons()
    

    
    # Estilo CSS para centralizar e arredondar a imagem
    st.markdown(
        """
        <style>
        .center {
            padding: 5x;
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

    # Adicionando a imagem com CSS
    # Defina o caminho para a pasta de arquivos estáticos
    static_path = os.path.join(os.getcwd(), 'assets', 'images')

    # Carregue a imagem
    image_path = os.path.join(static_path, 'rocket-gov.jpg')
    if os.path.exists(image_path):
        st.markdown(
            f"""
            <div class="center">
                <img src="data:image/jpg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" alt="Imagem arredondada" class="round-img">
                <div class="titles">
                    <h4>Subtítulo H3</h4>
                    <h1>Título Principal H1</h1>
                    <h5>Descrição em H5</h5>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error('Imagem não encontrada')

    # Texto abaixo da imagem
    ##st.markdown("## Teste de Nome Completo")
    time.sleep(10)



   

