n = input('Informe um número de 0 a 9999: ')
zeros = n.zfill(4)
digito = [int(d) for d in str(zeros)]


unidade = digito[-1]
dezena = digito[-2]
centena = digito[-3]
milhar = digito[-4]

print(f'A unidade é {unidade}')
print(f'A dezena é {dezena}')
print(f'A centena é {centena}')
print(f'A unidade de milhar é {milhar}')