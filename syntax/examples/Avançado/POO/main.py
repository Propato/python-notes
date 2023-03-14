from Animals import Animal
from Cachorro import Cachorro

animal = Animal('bolt', 'caramelo', 'ração')

animal.comer()
animal.movimento()

dog = Cachorro('Julie', 'caramelo', 'ração', 'F')

print(dog)
print(animal)

#set configurado com @property
animal.nome = 'aaaa'

print(animal)