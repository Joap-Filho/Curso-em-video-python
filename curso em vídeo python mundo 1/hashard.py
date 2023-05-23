def soma_digitos(numero):
    soma = 0
    while numero > 0:
        ultimo_digito = numero % 10
        soma += ultimo_digito
        numero //= 10
    return soma

def eh_harshad(numero):
    soma = soma_digitos(numero)
    return numero % soma == 0

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

for i in range(1, numero2+1):
    if eh_harshad(i) and i <= numero1:
        print(i)
