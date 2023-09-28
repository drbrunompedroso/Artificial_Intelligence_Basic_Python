import math

def circulo(raio):
    area  = float (math.pi * (raio ** 2))
    print('Área do circulo: ', round(area, 2))
    
    if area >= 0 and area <= 20:
         print('Área entre 0 e 20')
    elif area > 20 and area <= 30:
        print('Área entre 0 e 30')        
    else:
        print('Área > 30')

def main():
    for i in range(4):
        raio = float(input('Informe o raio:'))
        circulo(raio)

main()