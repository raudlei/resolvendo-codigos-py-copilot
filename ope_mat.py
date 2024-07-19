# Solicita como entrada dois números inteiros do usuário
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

# Solicita o operador para realizar a operação desejada
operacao = input("Digite o operador: (+)Soma - (-)Subtração - (*)Multiplicação - (/)Divisão: ")

# Realiza a operação com base no operador fornecido
if operacao == '+':
    resultado = num1 + num2
    operador = "+"
elif operacao == '-':
    resultado = num1 - num2
    operador = "-"
elif operacao == '*':
    resultado = num1 * num2
    operador = "*"
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        operador = "/"
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operador inválido"

# Exibe o resultado da operação
if isinstance(resultado, (int, float)):
    print(f"O resultado de {num1} {operador} {num2} é: {resultado}")
else:
    print(resultado)
