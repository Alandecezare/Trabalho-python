nomedovendedor= (input("Solicite o nome do vendedor "))
numerodecarrosvendidos = int(input("Solicite o número de carros vendidos "))
valortotaldevendas= int(input("Solicite o valor total de vendas "))
calculo= numerodecarrosvendidos*50.00
comissao=calculo* 0.5
salario= calculo+comissao+500
print(f"{nomedovendedor} , o seu salário é" , salario)