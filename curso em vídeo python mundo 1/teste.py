r1 = float(input('Informe o valor da primeira reta: '))
r2 = float(input('Informe o valor da segunda reta: '))
r3 = float(input('Informe o valor da terceira reta: '))

if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    print('Pode formar um triêngulo')
else:
    print('Não pode formar um')