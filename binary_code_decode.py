import random
import math

def calculate_num_steps(chromosome_length):
    return 2 ** chromosome_length

def calculate_step_size(min_value, max_value, num_steps):
    return (max_value - min_value) / num_steps

def calculate_lenght(min_value, max_value, precision):
    argument = 10 ** precision
    length = math.log2((max_value * argument) - (min_value * argument))
    length = math.ceil(length)
    return int(length)

# Función para codificar una solución en un cromosoma binario
def encode_solution(solution, chromosome_length, step_size, min_value):
    chromosome = ""
    for dimension in solution:
        # Convertir el valor en la dimensión en un paso discreto
        step = int(round((dimension - min_value) / step_size))
        # Convertir el paso discreto en una cadena binaria
        binary = bin(step)[2:].zfill(chromosome_length)
        chromosome += binary
    return chromosome

# Función para decodificar una solución a partir de un cromosoma binario
def decode_solution(chromosome, chromosome_length, min_value, step_size):
    solution = []
    for i in range(0, len(chromosome), chromosome_length):
        # Obtener la cadena binaria para la dimensión actual
        binary = chromosome[i:i+chromosome_length]
        # Convertir la cadena binaria en un paso discreto
        step = int(binary, 2)
        # Convertir el paso discreto en un valor en la dimensión
        dimension_value = min_value + (step * step_size) + (step_size / 2)
        solution.append(dimension_value)
    return solution


""" 
calculate_lenght(-5.12,5.12,3)
# Ejemplo de uso
# Crear una solución aleatoria
solution = [random.uniform(min_value, max_value) for i in range(10)]
# Codificar la solución en un cromosoma binario
chromosome = encode_solution(solution)
# Decodificar el cromosoma binario para obtener la solución
decoded_solution = decode_solution(chromosome)

# Imprimir la solución original, el cromosoma binario y la solución decodificada
print("Original solution:", solution)
print("Chromosome:", chromosome)
print("Decoded solution:", decoded_solution) """