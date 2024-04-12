# O código abaixo é uma tentativa de criar uma calculadora de Índice de Massa Corporal (IMC).
# No entanto, ele está incompleto e contém erros.
# Modifique o código para que ele solicite ao usuário seu peso em quilogramas e altura em metros.
# Seu programa deve calcular e imprimir o IMC do usuário seguindo a fórmula IMC = peso / (altura ** 2).
# Além disso, deve classificar o resultado em: Baixo peso, Peso normal, Sobrepeso ou Obesidade, 
# baseando-se nos valores de IMC.

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso/(altura * altura)  # Cálculo do IMC precisa ser corrigido

# Classificação do IMC (faltam informações)
if imc < 18.5:
    classificacao = "Baixo peso"
elif imc >= 18.5 and imc <= 24.99:
    classificacao = "normal"
elif imc >=25 and imc <= 29.99:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Seu IMC é {imc:.2f} e sua classificação é: {classificacao}")