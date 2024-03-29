N1 = int(input("Digite a nota da primeira avaliação: "))

# Define a média de aprovação
MEDIA = 7

# Calcula a nota necessária na segunda avaliação para a aprovação
N2 = ((MEDIA * 3) - N1) / 2

# Retorna ao usuário o valor que ele deve ter na nota 2 para ser aprovado
print("O valor que você deve ter na segunda avaliação para ser aprovado é:", N2)