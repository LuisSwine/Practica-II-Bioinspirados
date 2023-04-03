import random

def seleccion_por_ruleta(population):
    
    #Obtenemos la longitud
    tam_poblacion = len(population)
    
    #Creamos una lista vacia donde iremos guardando los indices de los padres
    indices = []

    # 1. Calcular la suma total de todos los valores de aptitud de la población.
    total_fitness = 0
    for individuo in population:
        individuo.encode()
        total_fitness += individuo.fitness    

    print(f"Total de fitness: {total_fitness}")

    # 2. Calcular la probabilidad de selección de cada individuo como su valor de aptitud dividido por la suma total de aptitudes.
    selection_probabilities = []
    for individuo in population:
        valor = individuo.fitness / total_fitness
        selection_probabilities.append(valor)

    for i in range(tam_poblacion):
        
        # 3. Generar un número aleatorio entre 0 y 1.
        r = random.uniform(0, 1)

        # 4. Iterar sobre la población y sumar las probabilidades de selección de cada individuo hasta que la suma sea mayor que el número aleatorio generado en el paso anterior.
        cumulative_probability = 0
        for i in range(len(selection_probabilities)):
            cumulative_probability += selection_probabilities[i]
            if cumulative_probability > r:
                selected_parent = i
                break

        # 5. Devolver el individuo correspondiente a la última probabilidad de selección sumada.
        indices.append(selected_parent)
    
    return indices
