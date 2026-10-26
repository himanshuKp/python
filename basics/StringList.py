stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro_words = []
sent_l=sent.split(" ")
for word in sent_l:
    if word not in stopwords:
        acro_words.append(word[:2].upper())
print(". ".join(acro_words))