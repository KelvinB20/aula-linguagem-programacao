import upper

nome = input("Digite seu Nome: ")
sobrenome = input("Digite seu Sobrenome: ")

print(nome[0].lower()+nome[1:].upper())
print(sobrenome[0].upper()+sobrenome[1:].lower())