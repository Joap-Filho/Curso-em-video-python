cores = {'fim': '\033[m', 'vermelho': '\033[0;31m', 'azul': '\033[0;34m', 'amarelo': '\033[0;33m'}

nome = str(input('\n\n\nQual o seu nome? '))

#Correções
nome_minusculo = nome.lower()
caps = nome.capitalize()
formatacao = nome_minusculo.strip()

#Correções
if formatacao == 'joão':
    print(f'Que nome bonito voê tem, {cores["azul"]}{caps.strip()}{cores["fim"]}!!!')
else: 
    print(f'Muito prazer, {cores["amarelo"]}{caps.strip()}{cores["fim"]}!!!')


