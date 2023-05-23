velocidade = float(input('Informe a velocidade do veículo: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você pagará a multa de R${multa:.2f}')
else: 
    print('Sem multas a pagar')