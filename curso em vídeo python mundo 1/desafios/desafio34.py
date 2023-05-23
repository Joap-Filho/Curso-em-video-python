salario = float(input('Informe o seu salário: R$'))
cores = {'fim':'\033[m','amarelo':'\033[0;33m','ciano':'\033[0;34m'}


if salario > 1250:
    aumento = salario * 0.10
    print(f'Seu salário foi aumentado em 10% ({cores["amarelo"]}R${aumento:.2f}{cores["fim"]}e ficou no valor de {cores["ciano"]}R${aumento + salario:.2f}{cores["fim"]}')

if salario <= 1250:
    aumento = salario * 0.15
    print(f'Seu salário foi aumentado em 15% ({cores["amarelo"]}R${aumento:.2f}{cores["fim"]} e ficou no valor de {cores["ciano"]}R${salario + aumento:.2f}{cores["fim"]}')