from random import randint

sorte = int(input('Informe um número de 1 a 5: '))
aleatorio = randint(1, 5)

if sorte == aleatorio:
    print('Parabéns, você acertou.')

if sorte >= 1 and sorte <= 5:
    while sorte != aleatorio:
        sorte = int(input('Você errou tente novamento: '))
        if sorte == aleatorio:
            print(f'Parabéns, você acertou! O número sorteado foi {aleatorio}.')
else:
    print('Um número de 1 a 5')



