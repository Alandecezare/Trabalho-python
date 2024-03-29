v = float(input("Digite o valor do produto: "))

d = v*0.10

nv = v-d

print(f"O valor do produto com desconto é de: {nv} ")
            
vp = nv/3
print(f"O valor de cada parcela em 3 vezes sem juros é de: {vp} ")  

c= nv*0.05
print(f"A comissão do vendedor caso a venda seja a vista será de:{c} ")          

c2= v*0.05
print(f"A comissão do vendedor caso a venda seja feita parcelada será de: {c2} ")