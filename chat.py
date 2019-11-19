from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Baymax')

conversa = ['oi','ola'
'qual seu filme favorito?','homem de ferro'
'qual seu personagem favorito?','Batman'
'me recomenda um filme de ação','velozes e furiosos'
'qual seu personagem favorito da vida real?','theRock'
'você gosta de filme de terro?','prefiro filme de aventura'
'qual seu estilo de filme ?','prefiro ação e aventura'
'quem é o theRock?', 'um ator renomado dos cinemas'
'cinema é seu lugar favorito?','claro,filmes são muit bons']

trainer = ListTrainer (bot)

trainer.train (conversa)

while True:
    pergunta = input("Você: ")

    resposta = bot.get_response(pergunta)
      
    if float(resposta.confidence) > 0.3:
        print('Baymax: ', resposta)
    else:
        print('Baymax: Não entendi')
   