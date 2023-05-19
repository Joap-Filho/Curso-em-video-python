n = input('Digite algo: ')
print(type(n))
alpha = (n.isalpha())
num = (n.isnumeric())
tudo_maiusculo = (n.isupper())
numero_e_letra = (n.isalnum())

if alpha == True:
    print(f'O dado {n} Contém somente letras')
if num == True:
    print(f'O dado {n} contém somente números')
if tudo_maiusculo == True: 
    print(f'O dado {n} apresenta todas as letras maiúsculas')
if numero_e_letra == True:
    print(f'O dado {n} apresenta letras ou números (Ou os dois também né vai saber) ')