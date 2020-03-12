import random
a = random.randint(1, 9)
c = "batata"
d = 0
while c != "exit":
    b = int(input("adivinhe o número gerado: "))
    if(b > a):
        print("muito alto, tente novamente ou digite 'exit' para sair \n")
    elif(b < a):
        print("muito baixo, tente novamente ou digite 'exit' para sair \n")
        d = d+1
    else:
        print("acertou mizeravi")
        d = d+1
        print("demorou ", d, " tentativas")
        c = "exit"
