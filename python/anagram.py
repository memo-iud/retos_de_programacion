"""ANAGRAMAS
Comprueba si dos cadenas de texto son anagramas 
si contienen el mismo número de caracteres
con la misma frecuencia pero en diferente orden"""

def are_anagrams (string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())
print(are_anagrams("Roma","Amor"))
print(are_anagrams("Amiga","Magia"))
print(are_anagrams("Hola","Mundo"))

