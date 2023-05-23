from random import randint
from time import sleep

sorteio = randint(0, 5)
palpite = int(input('Informe seu palpite: '))

while palpite != sorteio:
    palpite = int(input('Você errou! Tente novamente: '))

if palpite == sorteio:
    print('PROCESSANDO...')
    sleep(0.5)
    print(f'Parabéns, você acertou! O número sorteado foi {sorteio}')  


