# -----------------------------------------------------
# CALCULADORA EM PYTHON
# OPERAÇÕES BÁSICAS
# -----------------------------------------------------


def soma(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def divisao(a, b):
    if b == 0:
        return "O divisor não pode ser igual a zero!"
    else:
        return a/b
    
def multiplicacao(a, b):
    return a*b

def exponenciacao(a,b):
    return a**b

def porcentagem(a,b):
    return (a*(b/100))




while True:
    print("\n---------CALCULADORA----------")
    print("Soma - 1")
    print("Mutiplicação - 2")
    print("Divisão - 3")
    print("Subtração - 4")
    print("Exponenciação - 5")
    print("Porcentagem - 6")
    print("Para Sair - 0")
    
    opcao = int(input("Escolha a operação desejada: "))
    if opcao == 0:
        break
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = soma(num1, num2)
        
    elif opcao == 2:
        resultado = multiplicacao(num1, num2)

    elif opcao == 3:
        resultado = divisao(num1, num2)
    
    elif opcao == 4:
        resultado = subtracao(num1, num2)
        
    elif opcao == 5:
        resultado = exponenciacao(num1, num2)
        
    elif opcao == 6:
        resultado = porcentagem(num1, num2)
    
    print("---------RESULTADO--------")
    print(f"Resultado = {resultado}")