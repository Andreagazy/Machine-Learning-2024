from sklearn. feature_extraction.text import TfidfVectorizer

with open('corpus.txt', 'r') as file:
    corpus = file.readlines()

# Inisiasi obyek TFidfVectorizer
vect = TfidfVectorizer(stop_words='english' )

# Pembobotan TF-IDF
resp = vect.fit_transform(corpus)

# Cetak hasil
print('Hasil TF-IDF' )
print(resp)

# Cetak token hasil stopword
print ('Hasil Token' )
print(vect.get_feature_names_out())