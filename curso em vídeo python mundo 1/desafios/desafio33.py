n1 = int(input('Informe um número: '))
n2 = int(int(input('Informe outro número: ')))
n3 = int(input('Informe outro número: '))

lista = [n1 , n2, n3]
maior = max(lista)
menor = min(lista)
ordem_crescente = sorted(lista)
ordem_decrescente = sorted(lista, reverse=True)

print(f'O menor valor digitado é {menor} e o maior é {maior}') 
print(f'Os números na ordem crescente são {ordem_crescente}')
print(f'A ordem descrente é {ordem_decrescente}')
