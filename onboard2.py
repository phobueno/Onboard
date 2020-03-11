i = int(input("Digite um numero: "))
a = i % 2
if (a == 0):
    if(i % 4 == 0):
        print("Multiplo de 4")
    else:
        print("numero par")
else:
    print("numero impar")
