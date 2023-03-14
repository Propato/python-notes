# conjuntos são desordenados
# nao pode acessar um elemento especifico e nem altera=lo, mas é possivel remover e adicionar elementos
# conjuntos nao repetem dois valores iguais

# set com {} inicia eles

meu_conjunto = {1, 2, 3, -1, -10}
print(meu_conjunto)

meu_conjunto.add(7)
meu_conjunto.add(1)
meu_conjunto.discard(-10)

print(meu_conjunto)

# concatenar dois ou mais conjuntos co | ou .union()
frutas = {"Banana", "Uva", "Abacaxi", "Tomate"}
legumes = {"Cenoura", "Pepino", "Chuchu", 'Abacaxi'}

feira1 = frutas | legumes
print('\nUnião com |:        ', feira1)

feira2 = frutas.union(legumes)
print('União com .union(): ', feira2)

# interseção de dois ou mais conjuntos com & ou .intersection()
inter1 = frutas & legumes
print('\nInterseção com &:              ', inter1)

inter2 = frutas.intersection(legumes)
print('Interseção com .intersection():', inter2)

# a diferença entre dopis conuntos (elemento de um q nao esta no outro) pode ser expressa com - ou .difference()
dif1 = frutas - legumes
print(dif1)

dif2 = legumes.difference(frutas)
print(dif2)

# é possivel usar o operador in em for loopings

