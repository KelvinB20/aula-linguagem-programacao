# O código abaixo tem alguns problemas e está incompleto! 
# Altere o código abaixo para que ele atue como uma calculadora
# O usuário deve digitar um valor, um operador e outro valor
# seu programa deverá imprimir na tela o resultado da operação
# Faça com que o seu programa funcione até que o usuário digite -1

valor1 = int(input("Digite o primeiro valor: "))
operador = input("Digite o operador: ")
valor2 = int(input("Digite o segundo valor: "))

resultado = 0
while valor1 != -1 and valor2 != -1 and operador != "-1":

    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1 - valor2
    elif operador == '*':
        resultado = valor1 * valor2
    elif operador == '/':
        resultado = valor1 / valor2
    else:
        print('operador inválido')
    print("Resultado: ", resultado,"\n")
    valor1 = int(input("Digite o primeiro valor: "))
    operador = input("Digite o operador: ")
    valor2 = int(input("Digite o segundo valor: "))