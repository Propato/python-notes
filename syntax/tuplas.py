# tuplas são listas de multiplos tipos de dados

# nao é possivel alterar as variaveis de uma tupla

tupla1 = ("teste", 1, True)
tupla2 = 'teste', 2, False

print(tupla1, tupla2, '\n')

print(tupla1[0], tupla1[1])

for variavel in tupla1:
    print(variavel)

# operador + serve para concatenar duas tuplas

comidas = ("coxinha", "pipoca", "bolo", "brigadeiro")
bebidas = ("água", "refri", "suco")

picnic = comidas + bebidas

print(picnic)