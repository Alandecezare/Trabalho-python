a1 = float(input(" valor investido pelo primeiro amigo: "))
a2 = float(input(" valor investido pelo segundo amigo: "))

a3 = float(input(" valor investido pelo terceiro amigo: "))

s = a1+a2+a3

vlrp = float(input("Digite o valor do premio: "))

print(f"O jogador A receberá {(a1/s)*vlrp} ")

print(f"O jogador B receberá {(a2/s)*vlrp} ")

print(f"O jogador C receberá {(a3/s)*vlrp} ")