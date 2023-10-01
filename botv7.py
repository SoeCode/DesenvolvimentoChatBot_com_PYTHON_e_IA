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

#versao 7
mensagem_usuario = input('Em que posso ajudar? ')

if mensagem_usuario.startswith('/'):
    comando = mensagem_usuario[1:]
    if comando == 'help':
        resposta = 'Sou um assistente virtual, como posso te ajudar?'
    else:
        resposta = 'Desculpe, não entendi sua pergunta. Por favor tente novamente'
else:
    resposta = enviar_mensagem(mensagem_usuario)

print(f'Resposta do chatGPT: {resposta}')