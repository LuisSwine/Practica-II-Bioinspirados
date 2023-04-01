import binary_code_decode as binary
import cromosoma


def stop_requeriment(global_solution, best_child, epsilon):
    #Evaluamos la funcion
    result = best_child.fitness
    
    #Evaluamos la diferencia 
    if abs(global_solution - result) <= epsilon: return False
    else: return True
    
def second_stop_option(last_best, last_worst, epsilon):
    
    best = last_best.fitness
    worst = last_worst.fitness
    
    diference = abs(best - worst)
    print(f"Diferencia: {diference}")
    
    if diference <= epsilon: return False
    else: return True