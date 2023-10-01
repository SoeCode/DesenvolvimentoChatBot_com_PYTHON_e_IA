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

#versao 9
conversa_anterior = """
Você: Olá, como posso te ajudar?
Modelo: Eu sou um assistente virtual treinado para responder suas perguntas sobre produtos.
Você: Qual é o seu nome?
Modelo: Meu nome é chatGPT. Como posso ajudá-lo hoje?
"""

mensagem_usuario = input('Em que posso ajudar? ')
conversa_atual = conversa_anterior + 'Voce' + mensagem_usuario

resposta = enviar_mensagem(conversa_atual)
print(f'Resposta do chatGPT: {resposta}')
