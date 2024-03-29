nome_aluno = input("Digite o nome do aluno: ")
nota_prova = int(input("Digite a nota da prova: "))
nota_qualitativa = int(input("Digite a nota qualitativa: "))

media = (nota_qualitativa + (nota_prova * 2)) / 3

print("a sua média final foi de" , media)