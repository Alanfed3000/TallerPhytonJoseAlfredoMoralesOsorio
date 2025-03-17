import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 10

print("Bienvenido al juego de Adivina el Número!")
print("Tienes 10 intentos para adivinar un número entre 1 y 100.")

while intentos < max_intentos:
    intento = input(f"Intento {intentos + 1}/{max_intentos}: Ingresa tu número: ")
    if intento.isdigit():
        intento = int(intento)
        if 1 <= intento <= 100:
            intentos += 1
            if intento == numero_secreto:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
            elif intento < numero_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
        else:
            print("Por favor, ingresa un número entre 1 y 100.")
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")
else:
    print(f"Lo siento, has agotado tus 10 intentos. El número secreto era {numero_secreto}.")
