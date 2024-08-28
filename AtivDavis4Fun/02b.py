import random
num = random.randint(1,3)
num_usuario = int(input("digite um número de 1 a 3: "))

if num_usuario < 1 or num_usuario > 3:
    print("número fora do intervalo, digite novamente.")
else:
    if num_usuario==num:
     print("acertou")
    else:
     print("errou")

     print("o número aleatório era: ", num)