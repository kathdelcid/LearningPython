# if 3 > 5:
#     print("Cinco es mayor que tres")
# else:
#     print("Tres es menor que cinco")

x = 5
y = 'Kathy'

#print(x, y)

email = 'holakathy@hotmail.com'
# print(email)

a, b, c = 'Harry', 'Louis', 'Liam'
#print(a, b, c)

valor1 = valor2 = valor3 = 'Kathy'
#print(valor1, valor2, valor3)

inicio = 'Hola '
final = 'mundo'
# print(inicio+final)

entero = 20
conDecimales = 20.8
complejo = 8j

#print(entero, conDecimales, complejo)

lista = [1, 2, 3, 1, 3, 6, 8]
lista2 = lista.copy()
lista.append(1997)
# lista.clear()
# print(lista, lista2.count(3))
# print(len(lista))
# print(len(lista2))

# Another way
largoLista = len(lista)
largoLista2 = len(lista2)
#print(largoLista, largoLista2)

# print(lista[0])

# delete the last item
lista.pop()
# print(lista)
lista.pop()
# print(lista)

# delete the selected item
lista.remove(2)
# print(lista)

# Reverse the elements of the list
lista.reverse()
# Sort the elements
lista.sort()
# print(lista)

tupla = ("Hola", "Kathy")
# print(tupla)
# print(tupla.count("Hola"))
# print(tupla.index("Kathy"))
# print(tupla[0])

listaDeTupla = list(tupla)
listaDeTupla.append("Guapa")
# print(listaDeTupla)

rango = range(8)
# print(rango)

diccionario = {
    "nombre": "Bolita",
    "sexo": "Macho",
    "edad": 5
}

# print(diccionario)
# print(diccionario['nombre'])

# print(diccionario.get('nombre'))
diccionario['edad'] = 4
# print(diccionario)
# print(len(diccionario))

diccionario["¿Le gustan las zanahorias?"] = 'Si'
# print(diccionario)

# diccionario.pop('sexo')
# print(diccionario)

# diccionario.popitem()
#copiaDiccionario = diccionario.copy()
copiaDiccionario = dict(diccionario)
#del diccionario['¿Le gustan las zanahorias?']
diccionario.clear()
#print(diccionario, copiaDiccionario)

TokyoRevengers = {
    "nombre": "Tokyo Rvengers",
    "temporadas": 1
}

ShingekiNoKyojin = {
    "nombre": "Shingeki no kyojin",
    "temporadas": 6
}

Anime = {
    "Tokyo Revengers": TokyoRevengers,
    "Shingeki no kyojin": ShingekiNoKyojin
}

print(Anime)

series = dict(nombre="Navidad", temporadas="8")
print(series)

verdadero = True
falso = False

print(verdadero, falso)
