nome = str(input('Qual seu nome? '))

maiusculas = nome.upper()
minusculas = nome.lower()
sem_espacos = nome.replace(' ', '')
lista = nome.split()
primeiro_nome = len(lista[0])
qt = len(sem_espacos)

print(minusculas)
print(maiusculas)
print(sem_espacos)
print(qt)
print(primeiro_nome)
