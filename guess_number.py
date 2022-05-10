import random

# Límite de intentos
triesLimit = 10
tries = 0

print('\nBienvenido, el sistema "pensará" un número entre N '
      f'y M y deberás adivinarlo. Contarás con {triesLimit} '
      'intentos para lograrlo\n')

# Determinar el límite inferior y superior
bottom = int(input("Introduce el valor de N: "))
top = int(input("Introduce el valor de M: "))

print("\n")

# Calcular el número
number = random.randint(bottom, top)

# Solicitar el número
guess = -1

while guess != number and tries < triesLimit:

    guess = int(input("Introduce el número: "))
    tries += 1

    if guess < number:

        print("Cerca! el número por adivinar es mayor.\n")

    elif guess > number:

        print("Cerca! el número por adivinar es menor.\n")

    print(f"Intentos disponibles: {triesLimit - tries}\n")

if tries == 0:
    print("Has alcanzado el número permitido de intentos, "
          "suerte para la próxima!\n")
else:
    print(f'\nFelicidades! adivinaste el número "{number}" en '
          f'{tries} intentos!\n')
