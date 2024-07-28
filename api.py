# https://console.groq.com/docs/quickstart

# O uso da api groq pode ser substituído pela api local sem grandes problemas apenas descomentando o código abaixo e apagando o posterior.

# from ollama import chat

# def chat_generater(dataset, comando):
#     response = chat(
#         model='llama3',
#         messages=[
#             {
#                 'role': 'user',
#                  "content": f"""Você é um assistente especializado em gerar códigos Python para análise de dados. Eu irei fornecer as colunas do meu dataset e o tipo de análise que quero realizar, o dataset já está devidamente importado com nome df. Seu trabalho é retornar apenas o código Python que seja no formato executável na formatação correta necessária para realizar essa análise, sem qualquer explicação adicional.

#                     Dataset:
#                         colunas: {dataset}

#                         Análise desejada:
#                         {comando}

#                         Por favor, gere o código Python necessário para realizar essa análise.
#                         """,
#             },
#         ],
#     )
#     return response['message']['content'].replace('`', '')


from groq import Groq

client = Groq(
    api_key=" chave da api do groq ", 
)


def chat_generater(dataset, comando):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"""Você é um assistente especializado em gerar códigos Python para análise de dados. Eu irei fornecer as colunas do meu dataset e o tipo de análise que quero realizar, o dataset já está devidamente importado com nome df. Seu trabalho é retornar apenas o código Python que seja no formato executável na formatação correta necessária para realizar essa análise, sem qualquer explicação adicional.

                Dataset:
                    colunas: {dataset}

                    Análise desejada:
                    {comando}

                    Por favor, gere o código Python necessário para realizar essa análise.
                    """,
        }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content.replace('`', '') # É sempre necessário tratar a string visto que codigo vem na maioria das vezes em formato markdown