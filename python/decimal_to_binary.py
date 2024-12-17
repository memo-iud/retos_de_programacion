"""DECIMAL A BINARIO
Crea un programa que se encargue de 
transformar un número decimal a binario
para realizar la transformacion tenemos que 
dividir el número entero entre 2 y quedarnos con el resto
así sucesivamente mientras el número sea mayor que cero"""

def decimal_to_binary(decimal: int) -> str:
    binary = ""
   
    while decimal > 0: 
        binary = f"{decimal % 2}{binary}"
        decimal //= 2 
        
    return "0" if binary == "" else binary

print("el Número en dinario es: ",decimal_to_binary(385))    

