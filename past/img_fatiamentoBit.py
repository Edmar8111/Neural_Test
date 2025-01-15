from time import sleep
from PIL import Image
import os

teste = '' 
img_bit = {'img0':[], 'img1':[]}

def perceptron_img(img_value):
    global teste
    resize_img = Image.open(img_value)
    
    if os.path.isfile('new_img.png'):
        img_value=resize_img.resize((800, 600))
        img_value.save('new_img0.png')

    else:
        img_value=resize_img.resize((800, 600))
        img_value.save('new_img.png')
    
    if os.path.isfile('new_img.png') and os.path.isfile('new_img0.png'):
        for ab in range(0, 2):
            if len(img_bit['img0'])==0:
                with open('new_img.png', 'rb') as file: 
                    file = file.read()
                    for a in range(0, len(file)):
                        img_bit['img0'].append(file[a])
            else:
                with open('new_img0.png', 'rb') as file: 
                    file = file.read()   
                    for a in range(0, len(file)):
                        img_bit['img1'].append(file[a])
        
print(bin(len(teste)))
perceptron_img('cao0.png')
perceptron_img('cao1.jfif')
validar=[]
negado=[]

print(len(img_bit['img0']))
print(len(img_bit['img1']))
for a in range(0, len(img_bit['img0'])if len(img_bit['img1'])>len(img_bit['img0']) else len(img_bit['img1'])):
    validar.append(True) if img_bit['img0'][a]==img_bit['img1'][a] else negado.append(False)
if os.path.isfile('new_img.png') and os.path.isfile('new_img0.png'):
    os.remove('new_img.png')
    os.remove('new_img0.png')
sleep(5)
print(f'Validado: {len(validar)}, Negado: {len(negado)}')