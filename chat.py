from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('TW Chat Bot')

conversa = ['oi', 'olá', 'olá, bom dia', 'bom dia', 'bom dia,como vai?', 'estou bem']

conversa2 = ['qual seu filme favorito?','eu gosto de batman', 'meu filme favorito é o homem de ferro','Você gosta do tony stark?', 'Você gosta de cinema?','cinema é muito legal']

trainer = ListTrainer (bot)

trainer.train (conversa)
trainer.train(conversa2)

while True:
    pergunta = input("Você: ")

    resposta = bot.get_response(pergunta)
      
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Não entendi')
   