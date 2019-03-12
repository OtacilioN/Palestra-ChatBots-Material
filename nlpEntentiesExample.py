import spacy
utf8stdout = open(1, 'w', encoding='utf-8',
                  closefd=False)

nlp = spacy.load('pt')
doc = nlp('Silvio Meira uma vez disse que o Porto Digital fica em Recife')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
