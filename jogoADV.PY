import random


print("**********************************")
print("Bem vindo ao jogo de adivinhação!")
print("**********************************")

NumSecreto = random.randrange(1,501)
NumTentativas = 1
rodada = 0

print("Qual nível de dificuldade você quer?")
print("[1] facíl")
print("[2] médio")
print("[3] difícil")

nivel = float(input("Escolha seu nivel: "))

if nivel == 1:
    NumTentativas = 10

elif nivel == 2:
    NumTentativas = 7

elif nivel == 3:
    NumTentativas = 5

elif nivel == 0:
    print("Escolha um nível entre 1 e 3")

else:
    print("Escolha um nível entre 1 e 3")



for rodada in range(1, NumTentativas + 1):
    print("Tentativa {} de {}". format (rodada, NumTentativas))
    NumUsuario = float(input("Digite seu número entre 1 e 500: "))

    if NumUsuario > 500 or NumUsuario < 1: 
        print("Digite um número entre 1 e 500")
        continue    
    
    
    if NumUsuario == NumSecreto:
        print("Você acertou!")
        break
    
    elif NumUsuario > NumSecreto:
        print("{} é maior que o número secreto.".format(NumUsuario))

    elif NumUsuario < NumSecreto:
        print("{} é menor que o número secreto.".format(NumUsuario)) 

    else:
        print ("Você errou!")

        NumTentativas = NumTentativas + 1

print("Fim do jogo")


