from random import shuffle
aluno = str(input('Informe o nome dos alunos separados por vírgulas: '))
lista_alunos = aluno.split(',')

shuffle(lista_alunos)

print(f'A ordem selecionada foi {lista_alunos}')