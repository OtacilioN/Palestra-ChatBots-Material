from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def main():
    chatbot = ChatBot('Chat AI')
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.portuguese")

    user_text = ""
    while(user_text != "sair"):
        user_text = input("Voce: ")
        response = chatbot.get_response(user_text).text.encode('utf-8')
        print(response.decode())


if __name__ == "__main__":
    main()