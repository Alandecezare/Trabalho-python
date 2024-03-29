c = float(input("Digite o comprimento do terreno em metros: "))


l = float(input("Digite a largura do terreno em metros: "))

pmt = float(input("Digite o preço do metro de tela em reais: "))
    
p = 2 * (c + l)
    

ct = p * pmt
    

print("O custo para cercar o terreno com tela será de R$", ct)