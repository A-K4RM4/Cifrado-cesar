def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    
    # Recorre cada carácter en el texto
    for caracter in texto:
        # Verifica si el carácter es una letra mayúscula
        if caracter.isupper():
            # Aplica el desplazamiento y maneja el desbordamiento
            resultado += chr((ord(caracter) + desplazamiento - 65) % 26 + 65)
        # Verifica si el carácter es una letra minúscula
        elif caracter.islower():
            # Aplica el desplazamiento y maneja el desbordamiento
            resultado += chr((ord(caracter) + desplazamiento - 97) % 26 + 97)
        else:
            # Si no es una letra, lo deja igual (por ejemplo, espacios o signos de puntuación)
            resultado += caracter
    
    return resultado

def descifrado_cesar(texto_cifrado, desplazamiento):
    # Para descifrar, simplemente usamos un desplazamiento negativo
    return cifrado_cesar(texto_cifrado, -desplazamiento)

# Ejemplo de uso
texto_original = "Hola, este es un mensaje secreto!"
desplazamiento = 3

# Cifrar el texto
texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print("Texto cifrado:", texto_cifrado)

# Descifrar el texto
texto_descifrado = descifrado_cesar(texto_cifrado, desplazamiento)
print("Texto descifrado:", texto_descifrado)
