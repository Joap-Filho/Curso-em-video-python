from math import sqrt
n1 = int(input('Digite um número: '))

#conta com import
raiz = sqrt(n1)

#conta sem o import
raiz2 = (n1 ** (1/2))

#resultado com o import
print(f'A raiz de {n1} é {raiz}')

#resultado sem o import
print(f'A raiz de {n1} é {raiz2}')
