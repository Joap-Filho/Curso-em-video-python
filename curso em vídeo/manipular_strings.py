frase = str(input('Digite uma frase: '))

char_inuteis = frase.strip()
qt = len(char_inuteis)
minusculo = frase.lower()
qt_A = minusculo.count('a')
qt_O = minusculo.count('o')
encontrar = minusculo.find('mo')
lista = char_inuteis.split()
hifen = '-'.join(lista)

print(f'Aa frase digitada contém {qt} caracteres')
print(f'A frase contém {qt_A} letras a')
print(f'A frase contém {qt_O} letras o')
print(f'{encontrar}')
print(minusculo)
print(char_inuteis)
print(hifen)    