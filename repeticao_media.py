nota1 = []
soma = int
cont = 0
soma = 0
nota = int(input("Digite a nota: "))
while nota != -1:
    nota1.append(nota)
    soma = soma+nota
    cont += 1
    nota = int(input("Digite a nota: "))

media = soma/len(nota1)

if media >= 7:
    print("Aluno aprovado!\nMédia: ",media)
else:
    print("Aluno reprovado!\nMédia: ",media)
