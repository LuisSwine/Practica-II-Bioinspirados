import binary_code_decode as binary
import cromosoma


def stop_requeriment(global_solution, best_child, epsilon):
    #Evaluamos la funcion
    result = best_child.fitness
    
    #Evaluamos la diferencia 
    if global_solution - result == epsilon: return False
    else: return True