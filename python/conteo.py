""" CADENAS INVERTIDAS Simula reto 1234567890. 
Crea funcion que cuente de 1 a 9, 
eliminando cada vez un digito y mostrando un espacio en blanco
en su lugar, de manera ascendente y descendente"""

for i in range(1, 10): 
    print((i - 1) * " ", end="")
    for j in range(i, 10):
        print(j, end="")
    print()    

for i in range(9, 0, -1):
    print((i - 1) * " ", end="")
    for j in range(i, 10):
        print(j, end="")
    print()     


    