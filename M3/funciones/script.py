import sys

def sumar_pares(numeros):
    suma = 0
    # Verifica si hay números en los argumentos
    if len(numeros) == 0:
        print("No has ingresado ningún número.")
    else:
        # Recorre cada número y verifica si es par
        for numero in numeros:
            # Verifica si el argumento es un número entero
            if numero.isdigit():
                num = int(numero)
                # Si es par, lo sumamos
                if num % 2 == 0:
                    suma += num
            else:
                print(f"'{numero}' no es un número entero válido.")
        print(f"La suma de los números pares es: {suma}")

# Toma los argumentos desde la terminal (excluyendo el nombre del script)

if __name__ == "__main__":
    numeros = sys.argv[1:]  # Excluir el nombre del archivo
    sumar_pares(numeros)