numero_1 = 5
numero_2 = 10
numero_3 = 3
#generar una funcion que sume dos numeros
def sumar_y_agregar_3(a, b):
    """
    Suma dos números y agrega 3 al resultado.
    argumentos:
    a: primer número
    b: segundo número
    retorna: suma de a, b y 3
    """
    c= 3 + a + b
    return c

resultado = sumar_y_agregar_3(numero_1, numero_2)
print("La suma es:", resultado) #18


resultado_2= sumar_y_agregar_3(numero_1, numero_3)

print("La suma es:", resultado_2) #11
