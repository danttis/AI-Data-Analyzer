# AI-Data-Analyzer

![](example.gif)
Esse projeto utiliza o modelo Llama 3 para realizar análises em qualquer dataset, oferecendo uma interface fácil de usar para explorar dados e gerar insights significativos.

## Funcionalidades

- **Análise de Dados**: Permite a análise de conjuntos de dados utilizando o poder do Llama 3.
- **Visualizações Interativas**: Gera gráficos interativos para melhor compreensão dos dados.
- **Interface de Usuário Simples**: Construída com Streamlit, oferecendo uma experiência intuitiva para o usuário.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte configurado:

- Acesso à API do Llama 3, seja localmente ou através de [Groq](https://console.groq.com/docs/quickstart) ou outras alternativas.
- Python 3.10 ou superior.
- Os seguintes pacotes Python devem estar instalados:

  - `streamlit`
  - `pandas`
  - `matplotlib`
  - `seaborn`

Você pode instalar os pacotes necessários usando o comando:

```bash
pip install streamlit pandas matplotlib seaborn
```

## Como Usar

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/danttis/AI-Data-Analyzer.git
   cd AI-Data-Analyzer
   ```
2. **Configure a conexão**

   - Configure a conexão com a API do modelo que deseje usar, no arquivo `api.py`.
     
3. **Execute o Aplicativo**:

   - Inicie o aplicativo Streamlit:

   ```bash
   streamlit run app.py
   ```
     
4. **Carregue seu Dataset**:

   - Use a interface do usuário para carregar o seu dataset e começar a análise.

## Exemplos de Uso

- **Análise Exploratória de Dados**: Identifique padrões, tendências e anomalias nos dados.
- **Visualizações Personalizadas**: Crie gráficos personalizados para destacar insights específicos.

## Observações:
-  O modelo não tem acesso aos dados, apenas aos nomes das colunas presentes e tipos e realiza alguma análise ou gera gráficos a partir do seu prompt baseado nessas informações, você pode modificar o prompt no arquivo `api.py`.
-  O arquivo usa a função `exec()` para executar códigos gerado pela LLM, o que pode ser visto como uma vulnerabilidade em alguns casos, existem opções mais sofisticadas para fazer o mesmo que esse projeto, uma dica é usar o [Chat2VIS](https://blog.streamlit.io/chat2vis-ai-driven-visualisations-with-streamlit-and-natural-language/) ou outras alternativas.
- Outras dependências podem ser exigidas durante a execução, você pode melhorar o prompt no arquivo api.py para gerar gráficos apenas com o matplotlib ou seaborn.
