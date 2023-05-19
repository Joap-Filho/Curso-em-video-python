numero = int(input('Informe um número: '))

if numero > 999 and numero < 10000:
    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10

    print(f'milhar: {milhar}')
    print(f'centena: {centena}')
    print(f'dezena: {dezena}')
    print(f'unidade: {unidade}')



