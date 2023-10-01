#PREPARANDO O AMBIENTE
import openai
openai.api_key = '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'

def enviar_mensagem(mensagem):
    resposta = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt=mensagem,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return resposta.choices[0].text.strip()

#Versão 1

mensagem_usuario = 'Olá, como posso te ajudar?'
resposta_chatgpt = enviar_mensagem(mensagem_usuario)

print(f'Resposta do Chat GPT: {resposta_chatgpt}')



'''
Versão 4

mensagem_inicial = """
Você: Olá, como posso te ajudar?
Modelo: Eu sou um assistente virtual treinado para responder suas perguntas sobre produtos.
"""

mensagem_usuario = 'Qual é o seu nome? '

resposta = enviar_mensagem(mensagem_usuario, temperature = 0.5)
'''

mensagem_inicial = """
Você: Olá, como posso te ajudar?
Modelo: Eu sou um assistente virtual treinado para responder suas perguntas sobre produtos.
"""

instrucao = 'Dê uma resposta detalhada sobre os recursos do produto'
mensagem_usuario = 'Quais são os recursos do produto?'

conversa_com_instrucao = mensagem_inicial + 'Você: ' + mensagem_usuario + '\nInstrução: ' + instrucao

resposta = enviar_mensagem(conversa_com_instrucao)