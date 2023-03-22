from locale import ABDAY_1, ABDAY_3
from Pessoas import Pessoa
from Times import Time

A1 = Pessoa('Carlin', 16, '121-434.10', 1)
A2 = Pessoa('Adedonha', 14,'123-433.12' , 4)

B1 = Pessoa('Fernando', 15,'876-765.33' , 7)
B2 = Pessoa('Craque', 17, '999-564.34', 10)

'''
print(A1)
print(A2)
print(B1)
print(B2)
'''

timeA = Time("Rua de Baixo")
timeB = Time('Tropa da Esquina')

timeA.setJogador(A1)
timeA.setJogador(A2)

timeB.setJogador(B1)
timeB.setJogador(B1)

print(timeA, timeB, '\n')

timeA.printJogadores()
timeB.printJogadores()