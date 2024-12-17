"""INDICE DE MASA CORPORAL
Crea una calculadora del 
indice de masa corporal"""


weight = float(input("Tu Peso en kg: "))
height = float(input("Tu Altura en metros: "))

imc = weight / (height ** 2)

print (f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Peso bajo")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")