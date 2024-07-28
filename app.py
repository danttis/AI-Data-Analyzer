import streamlit as st
from api import chat_generater
from funcoes import retonar_info, captura_saida
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use 'Agg' para evitar erros de backend no Streamlit
import matplotlib.pyplot as plt

# Usando decorator para alterar comportamento da função  exec() e captura saída
@captura_saida
def executar_codigo(codigo):
    exec(codigo)

st.set_page_config(
    page_title="Analisador de Dados com IA",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Selecionar arquivo
data_file = st.sidebar.file_uploader("Carregar arquivo CSV")


# Caso as opções avançadas não sejam selecionadas, o padrão de leitura do csv é separado por vírgula e ponto para os decimais
separator, decimal_point = ',', '.'

# Opções avançadas para leitura do arquivo
show_additional_options = st.sidebar.checkbox("Opções Avançadas")

if show_additional_options:
    separator = st.sidebar.selectbox("Separador", [',', ';', '.', '|', ' '])
    decimal_point = st.sidebar.selectbox("Decimal", ['.', ','])

if data_file is not None:
    df = pd.read_csv(data_file, sep=separator, decimal=decimal_point)
    st.table(df.head())

    # Salvando as informações sobre os dados, nome das colunas e tipo de variável de cada coluna
    descricao_df = retonar_info(df)

# Recebe o texto digitado na interface
prompt = st.chat_input('Prompt')

if prompt:
    # Se algum texto foi digitado ele é passado para a função chat_generater do arquivo api junto com as informações do dataset
    analise = chat_generater(descricao_df, prompt)
    
    # A LLM gera um código em Python e é necessário executá-lo e capturar seu resultado
    resultado = executar_codigo(analise)
    st.write(resultado)

    # Não é possível capturar as imagens, mas como o gráfico foi executado, é possível salvá-lo e exibi-lo
    # Verificar se o código gerado cria gráficos
    if "plt.show()" in analise:
        # Salvar e exibir o gráfico gerado
        plt.savefig("plot.png")
        st.image("plot.png")

