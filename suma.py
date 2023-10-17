def sumar_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma
lista_numeros = [100, 400, 600, 800, 1000]
resultado = sumar_numeros(lista_numeros)
print("El resultado de la suma es:", resultado)