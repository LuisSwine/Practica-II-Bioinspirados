#Importamos los modulos del proyecto
import funciones_de_prueba as functions
import binary_code_decode as coder
import operador_cruza as cruza
import mutacion_code as mutacion
import reparation_mod as reparation
import stop_requeriment as sr
import parents_selection as ps
import survivors_selection as ss
import poblacion
import cromosoma

def algoritmoGenetico(dimensiones, lim_inf, lim_sup, tam_poblacion, funcion, cruza_method, prob_mutacion):
  
  #PRIMERO GENERAMOS LA POBLACION INICIAL
  poblacion_inicial = poblacion.Poblacion(tam_poblacion, dimensiones, lim_inf, lim_sup)
  poblacion_inicial.inicializarPoblacion()
  poblacion_inicial.setAllFitness(funcion)
  poblacion_inicial.printPoblacion()
 
  #CREAMOS LOS LISTADOS DE CONTROL
  mejores = []
  peores = []
  promedio = []
  
  mejores.append(poblacion_inicial.getBest(funcion))
  peores.append(poblacion_inicial.getWorst(funcion))
  val_prom = (mejores[0].fitness + peores[0].fitness) / 2
  promedio.append(val_prom)  
  
  while sr.stop_requeriment(0, mejores[len(mejores) - 1], 0.001):
    
    #CREAMOS LAS PAREJAS OBTENIENDO LA LISTA DE INDICES SELECCIONADOS EN ESTE CASO POR RULETA
    indices_padres = ps.seleccion_por_ruleta(poblacion_inicial.poblacion)
    print(f"Indices: {indices_padres}")

    #APLICAMOS LA CRUZA
    hijos = []
    if cruza_method == 1:
      hijos  = cruza.cruza_dos_puntos(poblacion_inicial.poblacion, indices_padres)
      print(f"Hijos: {hijos}")
      
    #Convertimos cada vector hijo en un objeto de la clase cromosoma para acceder a todos sus atributos
    cromosomas_hijos = []
    for hijo in hijos:
      new_hijo = cromosoma.Cromosoma(lim_inf, lim_sup, dimensiones, poblacion_inicial.step_size, poblacion_inicial.num_steps, poblacion_inicial.cromosomas_length)
      new_hijo.vector_solution = hijo
      new_hijo.ajustarValores()
      cromosomas_hijos.append(new_hijo)
    hijos = []
    
    #Ahora aplicamos la mutación a cada hijo
    for hijo in cromosomas_hijos:
      #Primero obtenemos la codificacion binaria del vector_solution
      binary_code = hijo.bin_code
      #Ahora aplicamos la mutación binaria
      mutated = mutacion.mutation_probabilistic(binary_code, prob_mutacion)
      #Asignamos el valor mutado al cromosoma
      hijo.bin_code = mutated
      #Hacemos la decodificacion para que los valores se ajusten al vector_solution
      hijo.decode()
      #Por ultimo ajusramos la mutacion para el cromosoma no quede fuera de los parametros
      hijo.ajustarValores()
      #Calculamos el fitness de cada hijo 
      hijo.evaluateFunction(funcion)
      #Agregamos los hijos mutados y ajustados a la poblacion
      poblacion_inicial.poblacion.append(hijo)
    
    #SELECCIONAMOS A LOS SOBREVIVIENTES
    poblacion_inicial.poblacion = ss.seleccion_sobrevivientes_torneo(poblacion_inicial.poblacion, tam_poblacion, 2)
    poblacion_inicial.printPoblacion()
    
    #Procedemos a sacar los mejores y peores candidatos
    mejores.append(poblacion_inicial.getBest(funcion))
    peores.append(poblacion_inicial.getWorst(funcion))
    val_prom = (mejores[-1].fitness + peores[-1].fitness) / 2
    promedio.append(val_prom)
    
      
    print(mejores[-1].fitness)
    print(peores[-1].fitness)
    
    input('PRESIONE...')
  pass

if __name__ == "__main__":
  
  dimensiones = 10
  lim_inf = -0.5
  lim_sup = 0.5
  tam_poblacion = 6
  function = functions.esfera
  cruza_method = 1
  prob_mutacion = 0.2
  
  algoritmoGenetico(dimensiones, lim_inf, lim_sup, tam_poblacion, function, cruza_method, prob_mutacion)

    



