qt = int(input('Quantas médias deseja calcular: '))
media_escola = str(input('É média escolar? (s/n) ')).lower()

#variáveis de controle
controle = 1
soma_notas = 0

for x in range (1, qt + 1):
    x = float(input(f'Digite a nota {controle}: '))
    soma_notas += x
    controle += 1

m = soma_notas / qt

if media_escola == 's':
    passar = float(input('Qual a média para ser aprovado? '))
    if m >= passar:
        print(f'Parabén, você passou com média {m:.2f}')
    else:
        print(f'Que pena, você reprovou com média {m:.2f}')

if media_escola == 'n':
    print(f'A média foi de {m}') 
