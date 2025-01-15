from random import randint
import numpy as np
from time import sleep

pontoA = False
pontoB = False
pontoC = False
gabarito = np.array([randint(0,1),randint(0,1)])
valores_alocados = []
def neuronio(input):
    for a in range(0,int(input)+1):
        valores_alocados.append(np.array([randint(0,100)%2, randint(0,100)%2]))

neuronio(10)
for b in range(0, len(valores_alocados)):
    print(True if list(valores_alocados[b]) == list(gabarito) else False, end='=> ')
    print(f'{b+1}ªépoca valores alocados: {valores_alocados[b]}, gabarito: {gabarito}')
    