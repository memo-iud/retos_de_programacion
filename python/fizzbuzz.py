"""EL FAMOSO FIZZ BUZZ
Escribe un programa que muestre por consola (con un print) 
los números del 1 al 100 (ambos incluidos y con un salto de linea entre cada impresión),
sustituyendo los sigientes:

Múltiplos de 3 por la palabra "fizz"
Múltiplos de 5 por la palabra "buzz"
Múltiplos de 3 y 5 a la vez por la 
palabra "fizzbuzz"
"""
for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
       print("fizzbuzz")
    elif number % 3 == 0:
       print("fizz") 
    elif number % 5 == 0:
       print("buzz")
    else:
       print(number)