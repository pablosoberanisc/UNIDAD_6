#Dado un diccionario de palabras y sus definiciones, busca la definición de una palabra específica. Si la palabra no se encuentra en el diccionario, retorna "No encontrada".
def buscar_definicion(diccionario, palabra):
    return diccionario.get(palabra, "No encontrada")
diccionario = {
    "Python": "Un lenguaje de programación de alto nivel.",
    "Java": "Un lenguaje de programación de propósito general.",
    "HTML": "Lenguaje de marcado utilizado para el desarrollo web."
}
palabra = "Java"
resultado = buscar_definicion(diccionario, palabra)
print(f"La definición de {palabra} es: {resultado}")
