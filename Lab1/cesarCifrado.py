import sys

def validar_parametros(texto, desplazamiento):
    # Validar que el texto no sea vacío.
    if not texto:
        raise ValueError("El texto no puede ser vacío.")

    # Validar que el desplazamiento sea un número entero.
    try:
        desplazamiento = int(desplazamiento)
    except ValueError:
        raise ValueError("El desplazamiento debe ser un número entero.")

    # Validar que el desplazamiento esté entre 1 y 26.
    if desplazamiento < 1 or desplazamiento > 26:
        raise ValueError("El desplazamiento debe estar entre 1 y 26.")

    return texto, desplazamiento

def cifrado_cesar(texto, desplazamiento):
    """
    Realiza el cifrado César con el desplazamiento indicado.

    Args:
        texto: El texto a cifrar.
        desplazamiento: El desplazamiento a aplicar.

    Returns:
        El texto cifrado.
    """

    # Obtener el alfabeto.
    alph = "abcdefghijklmnopqrstuvwxyz"

    # Inicializar el texto cifrado.
    cifrado = ""

    # Iterar sobre el texto.
    for letra in texto:
        # Ignorar los espacios.
        if letra.isspace():
            continue

        # Obtener la posición de la letra en el alfabeto.
        posicion = alph.find(letra)

        # Aplicar el desplazamiento.
        posicion = (posicion + desplazamiento) % len(alph)

        # Agregar la letra cifrada al texto cifrado.
        cifrado += alph[posicion]

    return cifrado

if __name__ == "__main__":
    # Obtener los argumentos del comando.
    texto = sys.argv[1]
    desplazamiento = sys.argv[2]

    # Validar los parámetros.
    texto, desplazamiento = validar_parametros(texto, desplazamiento)

    # Cifrar el texto.
    cifrado = cifrado_cesar(texto, desplazamiento)

    # Imprimir el texto cifrado.
    print(cifrado)