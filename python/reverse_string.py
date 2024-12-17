"""CADENA INVERTIDA
Crea una función que resiba un texto y lo invierta """

def reverse_string (text):
    reversed_string = "" 
    for char in text:
        reversed_string = char + reversed_string
    return reversed_string    

print(reverse_string("Hola mundo¡"))
