import numpy as np

#DEFINIMOS LA FUNCION DE ESFERA
def esfera(x):
  sumatoria = 0
  for i in range(len(x)):
    sumatoria += x[i] ** 2
  
  return sumatoria

#DEFINIMOS LA FUNCION DE ROSENBROCK
def rosenbrock(x):
  sumatoria = 0
  for i in range(len(x)-1):
      sumatoria += 100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
  return sumatoria

#DEFINIMOS LA FUNCION DE ACKLEY
def ackleyFunction(x):
    n = len(x)
    a = 20
    b = 0.2
    c = 2*np.pi
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += x[i]**2
        sum2 += np.cos(c*x[i])
    term1 = -a * np.exp(-b * np.sqrt(1/n * sum1))
    term2 = -np.exp(1/n * sum2)
    return term1 + term2 + a + np.exp(1)