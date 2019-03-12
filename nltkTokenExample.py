import nltk
utf8stdout = open(1, 'w', encoding='utf-8',
                  closefd=False)

sentence = "O Rec.ai é um evento arretado. Valeu pessoal!"
splited = sentence.split()
tokens = nltk.word_tokenize(sentence)

print("\n\nA versão com split", file=utf8stdout)
print(splited, file=utf8stdout)

print("\n\nA versão com tokens", file=utf8stdout)
print(tokens, file=utf8stdout)
print("\n")
