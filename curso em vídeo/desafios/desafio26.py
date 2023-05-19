frase = str(input('DIgite uma frase: '))
ocorrencia = str(input('Qual letra deseja encontrar?  ')).lower()

frase_formatada = frase.strip()
frase_minuscula = frase_formatada.lower()
contador_ocorrencia = frase_minuscula.count(ocorrencia)
primeiro_ocorrência = frase_minuscula.find(ocorrencia)
ultima_ocorrencia = frase_minuscula.rfind(ocorrencia)


print(f'Na frase {frase_formatada} a letra {ocorrencia} se repete {contador_ocorrencia} vezes') 
print(f'A primeira  ocorrência da letra {ocorrencia} aparece na posição {primeiro_ocorrência + 1}')
print(f'A última  ocorrência da letra {ocorrencia} aparece na posição {ultima_ocorrencia + 1}')

