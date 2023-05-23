nome = str(input('Qual seu nome Completo? '))

separacao = nome.split()
primeiro_nome = separacao[0]
ultimo_nome = separacao[-1]

print(f'{primeiro_nome} {ultimo_nome}')
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')  