#while segue o mesmo padrão em Python
# while 'Alguma condição':
#     'Alguma instrução'

i=0
while i<5:
    print(i)
    i+=1

#for é ussado para percorrer listas
nomes = ['david', 'monike', 'andre', 'matheus']

for nome in nomes:
    print(nome)

#funcao range serve para criar uma sequência de inteiros entre um intervalo
    # range(valor_inicial, valor_final, passo)

for x in range(3, 10, 2):
    print(x)

# CONTINUE E BREAK
    # Continue faz voltar para o inicio do loop
    # break continua o mesmo