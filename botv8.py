#integrando com outra API

import openai
import requests

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

def obter_resposta_da_api(pergunta):
    resposta = requests.get(f'https://api.example.com/perguntas?pergunta={pergunta}')
    return resposta.json()['resposta']

mensagem_usuario = 'Qual capital da Itália? '

if mensagem_usuario.startswith('/api'):
    pergunta = mensagem_usuario[5:]
    resposta = obter_resposta_da_api(pergunta)
else:
    resposta = enviar_mensagem(mensagem_usuario)

print(f'Resposta do chatGPT: {resposta}')