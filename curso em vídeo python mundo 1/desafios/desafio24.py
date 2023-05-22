cidade = str(input('Informe o nome da sua cidade: '))

organizado = cidade.title()
sem_espacos = organizado.strip()
minuscula = sem_espacos.lower()
santo = minuscula.split()

if santo[0] == 'santo': 
    print(f'Sua cidade cidade {sem_espacos} começa com Santo')
else: 
    print('Não começa com Santo ô BABACA')