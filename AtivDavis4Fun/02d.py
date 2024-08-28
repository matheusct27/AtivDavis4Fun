import random
acertos = 0
erros = 0

for i in range(5):

  num = random.randint(1,3)
  num_usuario = int(input("digite um número de 1 a 3: "))


  if num_usuario < 1 or num_usuario > 3:
    print("número fora do intervalo, digite novamente.")
  else:
    if num_usuario==num:
     print("acertou")
     acertos +=1
    else:
     print("errou")

     print("o número aleatório era: ", num)

     print()
print("O total de acertos foi: ", acertos)
