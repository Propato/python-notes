##scanf do Python
nome = input("Qual seu nome? ")
idade = int(input("E sua idade? "))

#printf formatado do Python
saudacao = f"Bom dia, {nome}, de {idade} ano(s)!"
print(saudacao)
#
# ou
#
print(f"Bom dia, {nome}, de {idade} ano(s)!", end=' _FINAL_ ')
print('\n*'*20)

    # a variavel end é a responsavel pelo ultimo caracter do print, que pelo padrao é um espaço