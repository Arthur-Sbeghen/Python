import random

numero = random.randint(1, 1000)
tentativas = 0

while True:
    palpite = input("Adivinhe o número entre 1 e 1000: ")
    try:
        palpite = int(palpite)
    except ValueError:
        print("\nPor favor, insira um número válido.\n")
        continue

    if palpite < 1 or palpite > 1000:
        print("\nO número deve estar entre 1 e 1000.\n")
        continue
    
    tentativas += 1
    if (palpite > numero):
        print("\nO número é menor.\n")
        continue
    elif (palpite < numero):
        print("\nO número é maior.\n")
        continue

    if palpite == numero:
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
        break
    else:
        print("Tente novamente.")