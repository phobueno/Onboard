num = int(input("Digite um numero: "))
check = int(input("Digite um numero para divisao: "))

a = num % check
if (a == 0):
    print("o resto da divisão é 0")
else:
    print("o resto da divisão não é 0")
