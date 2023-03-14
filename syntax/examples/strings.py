#STRINGS SAO LISTA DE CHAR
 #ENTAO TODAS AS FUNCOES DE LISTAS PODEM SER UUSADAS COM STRINGS

#deixa tudo minusculo
frase = "ISSO É UMA STRING"
frase_modificada = frase.lower();
print(frase_modificada, frase_modificada.islower())
#pergunta se esta tudo minusculo

#deixa tudo maiusculo
frase = "está tudo pequeno"
frase_modificada = frase.upper();
print(frase_modificada, frase_modificada.isupper())
#pergunta se esta tudo maiusculo

#limpa o inicio e final da palavra
palavra = " Introcomp  ".strip()
print(palavra)

#checa se uma string tem apenas letras
alpha = 'aa12 3-aa'
print(alpha.isalpha())

#como strings sao listas, é possivel repartir uma frase em uma lista de palavra
frase = frase.split()
print(frase)