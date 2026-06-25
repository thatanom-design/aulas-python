import random

numero = random.randint(1, 100)

while True: 
    palpite = int(input("escolha um numero entre 1 e 100"))

    if palpite == numero:
        print("Parabéns você acertou!")

    elif palpite < numero:
        print("o numero é Maior!")

    else:
        print("o numero é Menor!")

