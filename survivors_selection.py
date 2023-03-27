import random

def seleccion_sobrevivientes_torneo(poblacion, tamano_seleccion, emparejamiento):
    seleccionados = []
    while len(seleccionados) < tamano_seleccion:
        subconjunto = random.sample(poblacion, emparejamiento)
        ganador = min(subconjunto, key=lambda x: x.fitness)
        seleccionados.append(ganador)
    return seleccionados
