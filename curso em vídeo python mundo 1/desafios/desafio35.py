r1 = float(input('Informe o valor da primeira reta: '))
r2 = float(input('Informe o valor da segunda reta: '))
r3 = float(input('Informe o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Pode formar um triângulo')
    if r1 == r2 == r3:
        print('E é Equilátero')
    if r1 != r2 != r3 and r1 != r3:
        print('E é escaleno')
    if (r1 == r2 != r3) or (r2 == r3 != r1) or (r1 == r3 != r2):
        print('E é isósceles')
    
else: 
    print('Não pode formar um triângulo')