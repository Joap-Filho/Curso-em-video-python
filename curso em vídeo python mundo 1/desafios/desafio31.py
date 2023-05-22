distancia = float(input('Qual a distância da viagem? '))

if distancia <= 200:
    valor = (distancia * 0.5)
    print(f'Sua viagem ficou no valor de R${valor:.2f}')
if distancia > 200:
    valor = (distancia * 0.45)
    print(f'Sua viagem ficou no valor de R${valor:.2f}')  