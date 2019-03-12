# Before execute run
# pip install -U spacy
# python -m spacy download pt

import spacy
utf8stdout = open(1, 'w', encoding='utf-8',
                  closefd=False)

nlp = spacy.load('pt')
my_doc = nlp('O Rec.ai é um evento arretado.')

for token in my_doc:
    print(token.orth_, token.pos_, file=utf8stdout)
