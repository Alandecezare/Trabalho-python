# Solicita ao usuário informar a nota da segunda avaliação
N2 = int(input("Digite a nota da segunda avaliação: "))

# Define a média de aprovação
MEDIA = 7

# Calcula a nota necessária na primeira avaliação para a aprovação
N1 = (MEDIA * 3) - (N2 * 2)

# Retorna ao usuário o valor que ele deve ter na primeira avaliação para ser aprovado
print("A nota necessária na primeira avaliação para ser aprovado é:", N1)