"""CALCULAR EL FACTORIAL DE UN NÚMERO
    Args:
        n (int): Número entero positivo del cual se calculará el factorial
    Returns:
        int: El factorial del número
    Raises:
        ValueError: Si el número es negativo
    Ejemplo: factorial(5) se calcula multiplicando ese numero * todos los enteros 
        positivos < que el explicación (1*1=1, 1*2=2, 2*3=6, 6*4=24, 24*5=120) = 120
    """

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El número debe ser positivo o cero")

    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

# Ejemplo de uso
if __name__ == "__main__":
    numero = 5
    print(f"El factorial de {numero} es: {factorial(numero)}")