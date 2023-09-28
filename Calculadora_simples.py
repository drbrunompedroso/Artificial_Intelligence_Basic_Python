import math

def calculadora():
    while (1):
        value1 = float (input('Valor de V1:'))
        oper = input('Operação matemática:')
        value2 = float (input('Valor de V2:'))
        
        if oper == '+':
            result = value1 + value2
            print('Resultado (soma)  = ',round(result,2),'\n')
            
        elif oper == '-':
            result = value1 - value2
            print('Resultado (subtração)  = ',round(result,2),'\n')
            
        elif oper == '*':
            result = value1 * value2
            print('Resultado (multiplicação)  = ',round(result,2),'\n')
            
        elif oper == '/':
            result = value1 / value2
            print('Resultado (divisão)  = ',round(result,2),'\n')
            
        else:
            print('Operação Incorreta')
        
calculadora()