import nltk

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
splited = sentence.split()
tokens = nltk.word_tokenize(sentence)

tagged = nltk.pos_tag(tokens)
print(tagged)
