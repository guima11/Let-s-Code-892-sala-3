from funcoes import soma, subtração, multiplicacao, divisao


num01 = float(input('Digite um numero:'))
num02 = float(input('Digite um 2 numero:'))
operacao = input("Insira a operação 'soma', 'subtracao', 'divisao', 'multiplicacao', '+', '-', '/', '*'")

if operacao == 'soma' or operacao == '+':
    resultado = soma(num01, num02)
elif operacao == 'subtracao' or operacao == '-':
    resultado = subtração(num01, num02)
elif operacao == 'multiplicacao' or operacao == '*':
    resultado = multiplicacao(num01, num02)
elif operacao == 'divisao' or operacao == '/':
    resultado = divisao(num01, num02)

print(f'O resultado da operação é {resultado}')
