nfatorial = int(input('Informe o número para cálculo do fatorial: '))
controle1 = 1
controle = nfatorial

for fatorial in range(nfatorial, 0, -1):
    if fatorial - 1 < 1:
        break
    else:
        print(f'{controle} x {fatorial - 1} = {controle * (fatorial - 1)}')
        controle *= fatorial - 1
        controle1 *= fatorial
print(f'O fatorial de {nfatorial} é {controle1}')