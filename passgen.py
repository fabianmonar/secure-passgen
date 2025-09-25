import string
import random

# Pedimos la longitud de la contraseña
longitud = int(input("Ingrese el tamaño de la contraseña (mínimo 4): "))

if longitud < 4:
    print("La contraseña debe tener al menos 4 caracteres.")
else:
    # Definimos los grupos de caracteres
    letras_may = string.ascii_uppercase
    letras_min = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Aseguramos que haya al menos un carácter de cada tipo
    contraseña = [
        random.choice(letras_may),
        random.choice(letras_min),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Completamos el resto de la contraseña
    todos_caracteres = letras_may + letras_min + numeros + simbolos
    contraseña += [random.choice(todos_caracteres) for _ in range(longitud - 4)]

    # Mezclamos la contraseña para que no siga un patrón
    random.shuffle(contraseña)

    # Convertimos la lista en string
    contraseña_final = ''.join(contraseña)

    print("La contraseña generada es:", contraseña_final)