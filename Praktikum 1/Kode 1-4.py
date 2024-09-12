from sklearn. preprocessing import OrdinalEncoder

# Inisiasi obyek Ordinal Encoder
oe = OrdinalEncoder()

# Definisikan data
# dalam bentuk 2d
data = [
    ['Politeknik Negeri Malang' ],
    ['Politeknik Elektronika Negeri Surabaya' ],
    ['Politeknik Negeri Jakarata' ],
    ['Politeknik Negeri Semarang' ]
]

# Transformasi Ordinal Encoder
transform_oe = oe.fit_transform(data)

print('Data Asli' )
print(data)

print('Data Transformasi One-Hot Encoder' )
print(transform_oe)