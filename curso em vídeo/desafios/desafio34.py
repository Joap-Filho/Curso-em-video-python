salario = float(input('Informe o seu salário: '))

if salario > 1250:
    aumento = salario * 0.10
    print(f'Seu salário foi aumentado em 10% ({aumento} e ficou no valor de {salario + aumento})')

if salario <= 1250:
    aumento = salario * 0.15
    print(f'Seu salário foi aumentado em 15% (R${aumento:.2f}) e ficou no valor de R${salario + aumento:.2f})')