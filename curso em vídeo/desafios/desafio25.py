nome = str(input('Qual o seu nome? '))
minuscula = nome.lower()
buscar_silva = minuscula.find('silva')

if buscar_silva >= 0:
    print('Tem Silva no nome')
else:
    print('Não tem Silva no nome')