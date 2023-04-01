import random

def seleccion_sobrevivientes_torneo(poblacion, tamano_seleccion, emparejamiento):
    #print("Torneo")
    seleccionados = []
    while len(seleccionados) < tamano_seleccion:
        subconjunto = random.sample(poblacion, emparejamiento)
        #for hijo in subconjunto: print(hijo.fitness)
        ganador = min(subconjunto, key=lambda x: x.fitness)
        #print(ganador.fitness)
        seleccionados.append(ganador)
        #input('presione...')
    return seleccionados

def seleccion_por_extincion(poblacion, tamano_seleccion):
    
    sorted_population = sorted(poblacion, key = lambda x: x.fitness)
    
    new_population = sorted_population[:tamano_seleccion]
    
    return new_population
