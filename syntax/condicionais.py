nome = input('Insira um nome: ')
nome = nome.lower().strip()

# and == &&
# or == ||
# not == !

#if, elif (else if) e else do Python
if nome == 'monike' or nome == 'david':
    print('Casalzão!')
elif nome == 'matheus':
    print("Amigao!")
else:
    print(f"Vai saber quem {nome} é...")