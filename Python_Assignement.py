# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

datos_estudiante = {
    "Name": "Ione",
    "Age": 49, # integer
    "average": 9.00, # float
    "course": "Python",
    "subjects": ["Dictionaries", "Tuples", "Lists"], # List
    "last_notes": (8, 9, 10), # Tuple
}

print(datos_estudiante)

from decimal import Decimal
promedio_decimal = Decimal(str(datos_estudiante["average"]))

print(promedio_decimal) # 9.0 conviete el promedio a decimal

# Exercise 2: Round your float up.

import math

price = 3.50
final_price = math.ceil(price) 

print(final_price) # 4

# Exercise 3: Get the square root of your float.

square_root = math.sqrt(price)

print(square_root) # 1.8708286933869707

# Exercise 4: Select the first element from your dictionary.

first_element = datos_estudiante["Name"]

print(first_element) # Ione

# Exercise 5: Select the second element from your tuple.

second_element = datos_estudiante["last_notes"][1]

print(second_element) # 9

# Exercise 6: Add an element to the end of your list.

datos_estudiante["subjects"].append("Sets")

print(datos_estudiante["subjects"]) # ['Dictionaries', 'Tuples', 'Lists', 'Sets']

# Exercise 7: Replace the first element in your list.

datos_estudiante["subjects"][0] = "Loops"

print(datos_estudiante["subjects"]) # ['Loops', 'Tuples', 'Lists', 'Sets']

# Exercise 8: Sort your list alphabetically.

datos_estudiante["subjects"].sort()

print(datos_estudiante["subjects"]) # ['Lists', 'Loops', 'Sets', 'Tuples']

# Exercise 9: Use reassignment to add an element to your tuple.

datos_estudiante = {"last_notes": (8, 9, 10)} # Diccionario con tupla
datos_estudiante["last_notes"] = datos_estudiante["last_notes"] + (7,) # Concatena el tuple original con el nuevo elemento

print(datos_estudiante["last_notes"]) # (8, 9, 10, 7)
