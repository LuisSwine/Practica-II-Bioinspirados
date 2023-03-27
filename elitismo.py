def elitismo(poblacion, funcion_evaluacion, n_elitismo):
    # Ordenar la población en función de la aptitud
    poblacion_ordenada = sorted(poblacion, key=lambda cromosoma: funcion_evaluacion(cromosoma))
    
    # Conservar las mejores soluciones de la población actual
    poblacion_elitista = poblacion_ordenada[:n_elitismo]
    
    return poblacion_elitista