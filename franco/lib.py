def try_me(palabra1, palabra2):

    # Convertimos ambas a minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    # Convertimos las cadenas a lista.
    palabra1 = list(palabra1)
    palabra2 = list(palabra2)
    # Las ordenamos
    palabra1.sort()
    palabra2.sort()
    # Convertir de vuelta a cadena
    palabra1 = "".join(palabra1)
    palabra2 = "".join(palabra2)
    # Y finalmente comprobar si son iguales
    return palabra1 == palabra2

# Solicitar al usuario las cadenas
texto1 = input("Ingresa un texto: ")
texto2 = input("Ingresa otra texto: ")
es_anagrama = try_me(texto1, texto2)
if es_anagrama:
    print(f"{texto1} es anagrama de {texto2}")
else:
    print(f"{texto1} NO es anagrama de {texto2}")


if __name__ == "__main__":
    #Cadenas de prueba
    palabra1, palabra2 = "Nacionalista", "Altisonancia"
    detector_anagramas = try_me(palabra1, palabra2)
    print(detector_anagramas)
