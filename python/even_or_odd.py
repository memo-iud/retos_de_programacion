"""PAR O IMPAR
Crea un programa que compruebe si
un número entero es par o impar"""

try:
    number = int(input ("Ingresa un número entero: "))

    if number % 2 == 0:
        print(f"El {number} es Par")
    else:
        print(f"El {number} es Impar")
except ValueError:
    print("Entrada no válida")