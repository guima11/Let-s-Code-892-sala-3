def soma(a,b):
    calculo = a + b
    return calculo

def subtração(a,b):
    calculo = a - b
    return calculo


def divisao(a,b):
    if b != 0:
        calculo = a/b
    
    elif b == 0:
        print('Divisão inválida! Denominador igual a zero!')
        calculo = 0
    return calculo

def multiplicacao(a,b):
    calculo = a*b
    return calculo