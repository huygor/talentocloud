#INICIO FUNÇÃO CALCULADORA
def calculadora(num1, num2, operac):
    if operac == 1:
        resultado = num1 + num2
    elif operac == 2:
        resultado = num1 - num2
    elif operac == 3:
        resultado = num1 * num2
    elif operac == 4:
        resultado = num1 / num2
    elif operac == 0:
        resultado = 0
    elif operac != (1, 2, 3, 4):
        resultado = "Essa opção não existe"

    return resultado
#FIM da funcição CALCULADORA
#INICIO While
while(True):
    print("CALCULADORA")
    num1 = float(input("Por favor, digite o primeiro número: "))
    num2 = float(input("Por favor, digite o segundo número: "))
    print("Digite: 1 - Soma | 2 - Subtração | 3 - Multiplicação  | 4 - Divisão | 0 - Sair")
    operac = float(input("Por favor, digite o primeiro número: "))

    if operac == 0:
        break
    else:    
        mostraResultado = calculadora(num1, num2, operac)
        print("Resultado:", mostraResultado)
#FIM While
