from sklearn. feature_extraction.text import TfidfVectorizer

corpus = [
'the house had a tiny little mouse',
'the cat saw the mouse',
'the mouse ran away from the house',
'the cat finally ate the mouse',
'the end of the mouse story'

]

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