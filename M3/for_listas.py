
lista = ['a', 'b', 'c', 'd', 'e']
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# for i in range(len(lista)):
#     print("el valor de i es:", i)
#     print(f"Elemento {i} de la lista: {lista[i]}")


# for i in lista:
#     print("el valor de i es:", i)
#     print(f"Elemento de la lista: {i}")

for clave, valor in diccionario.items():
    print("la clave es:", clave)
    print(f"El valor de la clave {clave} y su valor es: {valor}")

# añadir un elemento al diccionario
diccionario['f'] = 6