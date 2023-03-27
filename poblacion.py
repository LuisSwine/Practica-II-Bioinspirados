import random

import binary_code_decode as coder
import cromosoma

class Poblacion:
    def __init__(self, tam_poblacion, dimensiones, lim_inf, lim_sup):
        
        self.dimensiones = dimensiones #Dimensiones o cantidad de variables de decision
        
        self.lim_inf = lim_inf #Limite inferior de las soluciones
        self.lim_sup = lim_sup #Limite superior de las soluciones
        
        #Creamos las variables de codificacion
        self.cromosomas_length = coder.calculate_lenght(lim_inf, lim_sup, 2)
        self.num_steps = coder.calculate_num_steps(self.cromosomas_length)
        self.step_size = coder.calculate_step_size(lim_inf, lim_sup, self.num_steps)
        
        self.poblacion = [] #Lista de individuos o cromosomas
        self.tam_poblacion = tam_poblacion #Cantidad de individuos de la poblacion
        
    def inicializarPoblacion(self):
        self.poblacion = []
        
        for i in range(self.tam_poblacion):
            new_cromosoma = cromosoma.Cromosoma(self.lim_inf, self.lim_sup, self.dimensiones, self.step_size, self.num_steps, self.cromosomas_length)
            new_cromosoma.randomInitialization()
            self.poblacion.append(new_cromosoma)
    
    def printPoblacion(self):
        for individuo in self.poblacion:
            individuo.printCromosoma()
    
    def setAllFitness(self, funcion):
        for individuo in self.poblacion:
            #Evaluamos la funcion
            individuo.evaluateFunction(function=funcion)
    
    def getBest(self, funcion):
        #Primero asignamos todos los fitness a cada cromosoma
        self.setAllFitness(funcion)
        poblacion_ordenada = sorted(self.poblacion, key= lambda x: x.fitness)
        best = poblacion_ordenada[0]
        return best
        
    
    def getWorst(self, funcion):
        #Primero asignamos todos los fitness a cada cromosoma
        self.setAllFitness(funcion)
        poblacion_ordenada = sorted(self.poblacion, key= lambda x: x.fitness)
        best = poblacion_ordenada[-1]
        return best
    