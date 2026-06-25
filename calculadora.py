print("=== Calculadora Pro ===")

a = float(input("Número 1: "))
b = float(input("Número 2: "))

operacao = input("Escolha (+, -, *, /): ")

if operacao == "+":
    print("Resultado:", a + b)

elif operacao == "-":
    print("Resultado:", a - b)

elif operacao == "*":
    print("Resultado:", a * b)

elif operacao == "/":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Erro: divisão por zero")

else:
    print("Operação inválida")
