cores = {'fim': '\033[m', 'azul': '\033[1;34m', 'vermelho': '\033[1;31m', 'amarelo': '\033[1;33m'}

casa = float(input(f'\n{cores["amarelo"]}Qual o valor da casa que você vai financiar?{cores["fim"]} '))
salario = float(input(f'{cores["amarelo"]}Qual o valor do seu salário? {cores["fim"]}'))
anos = float(input(f'{cores["amarelo"]}Em quantos anos você deseja pagar? {cores["fim"]}'))

#contas
meses = int(anos * 12)
prestacao = casa / meses
porcent = prestacao * 0.30

if porcent <= salario:
    print(f'{cores["azul"]}Parabéns, você poderá realizar o empréstimo, e as prestações ficarão no valor de {cores["amarelo"]}R${prestacao:.2f}{cores["fim"]}')
if porcent > salario:
    print(f'{cores["vermelho"]}Infelizmente você não poderá realizar o empréstimo.{cores["fim"]}')


