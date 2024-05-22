#Dado un arreglo ordenado de números enteros, encontrar la posición de un número específico usando búsqueda binaria. Si el número no se encuentra en el arreglo, retornar -1.
def busqueda_binaria(arr, objetivo):
    izquierda = 0
    derecha = len(arr) - 1  
    print(derecha)
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
arr = [3, 10, 20, 25, 32, 40, 45, 50]
objetivo = 32
resultado = busqueda_binaria(arr, objetivo)

print(f"El objetivo {objetivo} se encuentra en el índice: {resultado}")
