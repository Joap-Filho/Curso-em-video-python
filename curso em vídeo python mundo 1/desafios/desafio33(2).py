a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c= int(input('Digite o terceiro valor: '))
menor = a
maior = a

# Condições do maior número
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor valor digitado foi {menor}')

#Condições do menor número
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor digitado foi {maior}')