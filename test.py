from random import randint


valores = []
gabarito = {'neural_1':[0,1], 'neural_2':[0,0]}
validar=0
epoca = 0
def init_a(qtd):
    global valores,validar, epoca
    for a in range(0,int(qtd)):
        epoca=a+1
        if len(valores)>0:
            if a-1 >= 1:
                valores.append([randint(0, 100)%2])
            valores[a-1].append(randint(0, 100)%2)
        if len(valores)==0:
            valores.append([randint(0, 100)%2])
       
    for b in range(0,len(valores)):
        print(f'{valores[b]}, {b+1}ªépoca')
        if valores[b] == gabarito['neural_1']:
            valor_0 = f'Sucesso, {b+1}ª época'
            valor_1 = f'Valor Transmissor:{valores[b]} Receptor:{gabarito["neural_1"]}'

    print(valor_0)
    
    print(valor_1)
        # if len(valores[f'neural_{a}']) >= 2:
        #     if validar==0:
        #         f'{validar+1}' if valores['neural_0'][0]==gabarito['neural_1'][0] and valores['neural_0'][1]==gabarito['neural_1'][1] else f'{validar}'            
        #         print(f'Neuro Transmissor:{valores["neural_0"][0],valores["neural_0"][1]}, Neuro Receptor:{gabarito["neural_1"][0],gabarito["neural_1"][1]}')
        #     return print('Sucesso')
init_a(10)