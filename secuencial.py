#Dado un arreglo desordenado de números enteros, encontrar la posición de un número específico. Si el número no se encuentra en el arreglo, retornar -1.
def busqueda_secuencial(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1
arreglo = [34, 7, 23, 32, 5, 62]
objetivo = 23
resultado = busqueda_secuencial(arreglo, objetivo)

print(f"El objetivo {objetivo} se encuentra en el índice: {resultado}")
