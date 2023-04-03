import random

import binary_code_decode as coder
import reparation_mod as ajust

class Cromosoma:
    def __init__(self, lim_inf, lim_sup, dimensiones, step_size, num_steps, cromosoma_length):
        
        #Carcateristicas
        self.vector_solution = []
        self.bin_code = ""
        self.fitness = 0
        
        #Variables para la codificacion
        self.step_size = step_size
        self.num_steps = num_steps
        self.cromosoma_length = cromosoma_length
        
        #Variables que se reciben
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.dimensiones = dimensiones
        
    def randomInitialization(self):
        #Inicializamos el vector solucion como una lista vacia
        self.vector_solution = []
        
        #Generamos los valores aleatorios dentro del rango de los limites del problema
        for i in range(self.dimensiones):
            self.vector_solution.append(random.uniform(self.lim_inf, self.lim_sup))
        
    def encode(self):
        self.bin_code = coder.encode_solution(self.vector_solution, self.cromosoma_length, self.step_size, self.lim_inf)
        return self.bin_code
        
    def decode(self):
        self.vector_solution = coder.decode_solution(self.bin_code, self.cromosoma_length, self.lim_inf, self.step_size)
        return self.vector_solution
    
    def setFitness(self, value):
        self.fitness = value
        
    def evaluateFunction(self, function):
        self.fitness = function(self.vector_solution)
    
    def printCromosoma(self):
        print(f"Datos del cromosoma: \n"
              + f"Vector solucion {self.vector_solution} \n"
              + f"Fitness {self.fitness}")
        
    def ajustarValores(self):
        self.decode()
        self.vector_solution = ajust.repair_solution(self.vector_solution, self.lim_inf, self.lim_sup)
        self.encode()