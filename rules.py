__author__ = "Otacilio Maia"
__version__ = "1.0.0"


def bot_answer(user_text):
    if(user_text == "Ligue a luz"):
        print("Bot: Luz ligada com sucesso")
    elif(("Ligue" in user_text or "Acenda" in user_text) and ("luz" in user_text or "lampada" in user_text)):
        print("Bot: Luz ligada com sucesso")
    elif (user_text == "sair"):
        return
    else:
        print("Bot: Nao entendi o que voce falou")


def main():
    user_text = ""
    while(user_text != "sair"):
        user_text = input("Voce: ")
        bot_answer(user_text)


if __name__ == "__main__":
    main()
