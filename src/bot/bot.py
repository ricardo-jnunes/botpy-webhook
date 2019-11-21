from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot(
    'Monitoring BotPy',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Ainda não sei responder esta pergunta.',
            'maximum_similarity_threshold': 0.5
        },{
            'import_path': 'bot.environment_adapter.EnvironmentLogicAdapter'
        }
    ])
conversation = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo',
                'Você gosta de programar?', 'Sim, eu programo em Python'
                'Obrigado', 'Não tem por onde.',
                'Você acha isso certo?', '¯\\_(ツ)_/¯']

trainer = ListTrainer(bot)
trainer.train(conversation)

def speak(question):
    return bot.get_response(question)


#while True:
#    pergunta = input("Usuário: ")
#    resposta = bot.get_response(pergunta)
#    print('Bot: ', resposta)
