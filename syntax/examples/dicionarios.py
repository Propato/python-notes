# armazena duas variaveis, uma sendo o nome do dado e outra sendo o valor do dado
# inserimos palavras chaves com seus respectivos valores (traduções)

# exemplo de declaração de um dicionario de pessoa
pessoa1 = {
    'cidade': "Marilândia",
    'nome': "Jaca Santos",
    'idade': 63
}
print(pessoa1)

# dicionarios vazios
dicionario_vazio = {}
dicionario_vazio = dict()

# Para acessarmos um valor do dicionário, devemos utilizar a sintaxe dicionário[palavra chave].
nome_pessoa = pessoa1['nome']
idade_pessoa = pessoa1['idade']

print(f"Olá, me chamo {nome_pessoa} e tenho {idade_pessoa} anos!")

# exemplo com multiplos tipos
notas = {
    "turma": "Introcomp 2021",
    10: ["Jaca", "Jorge"],     # alunos que tiraram nota 10
    7: ["Ze", "Maria"],        # alunos que tiraram nota 7
    5: ["Joao"],               # alunos que tiraram nota 5
    "quantidade": 5
}

print(notas)

# exemplo de criação de dicionario, inserindo palavra chave e o valor
alunos = {}

for i in range(2):
  n_matricula = int(input("Digite um número de matrícula: "))
  aluno = input("Digite o nome do aluno: ")

  alunos[n_matricula] = aluno

print(alunos)

matricula_escolhida = int(input("Escolha um número de matrícula: "))

print(alunos[matricula_escolhida])

# funções

#pop reove um item
notas.pop(10)
print(notas)

#len retorna tamanho
print(len(notas))

# operador in checa as palavras chaves do dicionario
#  para checar os valores devemos usar o método .values()

# para concatenar dois dicionarios usamos:
#   dicionario1.update(dicionario2)