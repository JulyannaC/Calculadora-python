def soma(a, b):
    return a + b

def subtração(a, b):
    return a - b

def multiplicação(a, b):
    return a * b

def divisão(a, b):
    return a / b

print("Selecione a operação que você deseja realizar:")
print("Soma [1]")
print("Subtração [2]")
print("Multiplicação [3]")
print("Divisão [4]")

escolha = int(input("Digite a sua operação:"))
while escolha not in [1,2,3,4]:
    print("Operação não é válida!")
    escolha = int(input("Digite a sua operação:"))


num1= float(input("Digite o primeiro número:"))
num2= float(input("Digite o segundo número:"))

if escolha == 1:
    print(soma(num1, num2))

elif escolha == 2:
    print(subtração(num1, num2))

elif escolha == 3:
    print(multiplicação(num1, num2))

elif escolha == 4:
    print(divisão(num1, num2))
