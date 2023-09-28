import math

def sensor_MODEL():
    while(1):
        print('*************************************************')
        print('Software para Previsão de Dados de Sensores')       
        signal = input('Entre com a Unidade de Medida Desejada (I/V):')

        if signal == 'I':
            imax = float (input('Imax:'))
            imin = float (input('Imin:'))
            levelTank = float (input('Capacidade do Tanque:'))
            signalSensor = float (input('Sinal Simulado (I):'))
            levelCalc = ((signalSensor - imin) / ((imax - imin)/levelTank))
            percent = (levelCalc/levelTank) * 100
            print('Nivel do Tanque:', round(levelCalc,2), 'L', '(',round(percent,2),'%)')
         

        elif signal == 'V':
            vmax = float (input('Vmax:'))
            vmin = float (input('Vmin:'))
            levelTank = float (input('Capacidade do Tanque:'))
            signalSensor = float (input('Sinal Simulado (V):'))
            levelCalc = ((signalSensor) / ((vmax - vmin)/levelTank))
            percent = (levelCalc/levelTank) * 100
            print('Nivel do Tanque:', round(levelCalc,2), 'L', '(',round(percent,2),'%)')
        
        else:
            print('INDICE INVÁLIDO')
            levelCalc = False
        
        if levelCalc != False:        
            if levelCalc <= (0.25 * levelTank):
                print('Bomba    B1 = 1 ')
                print('Valvula  V1 = 1')
                print('Bomba    B2 = 0')
                print('Valvula  V2 = 0')
                print('Valvula  V3 = 0')
                
            elif levelCalc > (0.25 * levelTank) and levelCalc <= (0.50 * levelTank):
                print('Bomba    B1 = 0')
                print('Valvula  V1 = 0')
                print('Bomba    B2 = 1')
                print('Valvula  V2 = 1')
                print('Valvula  V3 = 0')
                
            elif levelCalc > (0.50 * levelTank) and levelCalc <= (0.75 * levelTank):
                print('Bomba    B1 = 1')
                print('Valvula  V1 = 1')
                print('Bomba    B2 = 1')
                print('Valvula  V2 = 1')
                print('Valvula  V3 = 0')
            
            elif levelCalc > (0.75 * levelTank):
                print('Bomba    B1 = 0')
                print('Valvula  V1 = 0')
                print('Bomba    B2 = 0')
                print('Valvula  V2 = 0')
                print('Valvula  V3 = 1')
        
sensor_MODEL()