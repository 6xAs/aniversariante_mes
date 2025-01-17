# Teste Imagem Arredondada 🎉

Esta aplicação Streamlit exibe uma imagem principal com bordas arredondadas e estilizadas, além de carregar e exibir dados de aniversariantes do mês a partir de um arquivo CSV.

## Funcionalidades

- Exibição de uma imagem principal com bordas arredondadas e estilizadas.
- Carregamento de dados de aniversariantes do mês a partir de um arquivo CSV.
- Conversão de imagens e GIFs para base64 para exibição na aplicação.

## Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas Python: `streamlit`, `pandas`, `requests`, `Pillow`

## Instalação

1. Clone o repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Como usar

1. Coloque o arquivo CSV com os dados dos aniversariantes na pasta [_datasets](http://_vscodecontentref_/0) e nomeie-o como `atores_aniversariantes.csv`.

2. Coloque as imagens e GIFs na pasta [gifs](http://_vscodecontentref_/1).

3. Execute a aplicação Streamlit:

    ```bash
    streamlit run 1_🎉main.py
    ```

4. Acesse a aplicação no seu navegador em `http://localhost:8501`.

## Estrutura do Projeto

```plaintext
.
├── _datasets
│   └── atores_aniversariantes.csv
├── assets
│   └── images
│       └── gifs
│           ├── confete_Right.gif
│           ├── confete_Left.gif
│           └── gif_background.gif
├── 1_🎉main.py
└── README.md