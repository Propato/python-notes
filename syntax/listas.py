
# <nome da variável que armazenará a lista> = [<elemento1>, <elemento2>, ..., <elementoN>]
carrinho = ["11", "22", "33", "44", "55", "66", "77", "88", "33"]
print('carrinho:', carrinho)

# fatia da lista
# lista[inicio:fim:passo]
fatia = carrinho[1:6:2]
print('fatia 1:', fatia)
#
fatia = carrinho[::-1]
print('fatia (lista) invertida:', fatia, '\n')

#tamanho da lista
tam = len(carrinho)
print('tamanho da lista:', tam, carrinho)

#contagem de quantas vezes um item aparece na lista
quant = carrinho.count('33')
print('quantidade q',33,'aparece na lista:', quant)

#maior e menor valor da lista
print('max valor da lista:', max(carrinho))
print('min valor da lista:', min(carrinho),'\n')

#adicionando itens ao final da lista
carrinho.append("99")
carrinho.append("1010")
print('carrinho atualizado:', carrinho, '\n')

#removendo itens
    #funcao pop() recebe indice do item a ser removido ou nao recebe nada (removera ultimo item)
c = carrinho.pop(5)
print(carrinho)
print('item removido:',c)

    #funcao remove() recebe item e realiza a busca na lista para removelo
    #item removido nao pode ser armazenado
carrinho.remove('1010')
print(carrinho)
print('item removido: 1010\n')

#Copiando itens de listas
    # listas funcionam como ponteiros para listas, entao fazer lista1 = lista2 faz elas apontarem pra mesma lista da memoria, porém usar a função faz elas armazenarem o mesmo conteudo mas em espaços de memoria diferente.

carrinho_c = carrinho
carrinho_copia = carrinho.copy()

print('listas copiadas:\n')
print(carrinho, '\n', carrinho_c, '\n', carrinho_copia)
carrinho.append('6')
print(carrinho, '\n', carrinho_c, '\n', carrinho_copia, '\n')

#ordenacao de listas
carrinho.sort()
print('carrinho ordenado:', carrinho)

carrinho = carrinho+carrinho+['aaa', 'bbb']
print(carrinho)