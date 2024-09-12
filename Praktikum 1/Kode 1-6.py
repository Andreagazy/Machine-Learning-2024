from sklearn.preprocessing import OneHotEncoder

# Inisiasi obyek OneHotEncoder
de = OneHotEncoder(drop='first')

# Definisikan data dalam bentuk 2D
data = [
    ['Politeknik Negeri Malang'],
    ['Politeknik Elektronika Negeri Surabaya'],
    ['Politeknik Negeri Jakarta'],
    ['Politeknik Negeri Semarang']
]

# Transformasi menggunakan OneHotEncoder
transform_de = de.fit_transform(data).toarray()

print('Data Asli')
print(data)

print('Data Transformasi OneHot Encoding')
print(transform_de)
