#Dada una lista de números enteros, contar la frecuencia de cada número utilizando una tabla hash.
def contar_frecuencia(lista):
    frecuencia = {}
    for numero in lista:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    return frecuencia
lista = [1, 2, 2,2, 2,2,2,2,2,2,2,2, 3, 3, 3, 4, 4, 4, 4]
frecuencia = contar_frecuencia(lista)
print("Frecuencia de cada número en la lista:")
for numero, count in frecuencia.items():
    print(f"{numero}: {count}")
