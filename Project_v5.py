#################################### FUNÇÕES###########################################
def menu_principal():
    print("*****************************************************************************************")
    print("*   Benvido ao nosso programa de cálculo!                                               *")
    print("*                                                                                       *")
    print("*   A nossa calculadora é capaz de converter números binários em decimais e vice-versa! *")
    print("*   Esperamos que goste!                                                                *")
    print("*                                                                                       *")
    print("*         !!! O nosso programa só é capz de calcular com números inteiros !!!           *")
    print("*                                                                                       *")
    print("*****************************************************************************************")
    print("*                                                                                       *")
    print("*   Realizado por: Artur Alves e Jinhua Chen                                            *")
    print("*   Turma: 12ºCE                                                                        *")
    print("*   Escola: Colégio Vasco da Gama                                                       *") 
    print("*   Disciplina: AIB                                                                     *")
    print("*   Professor: Pedro Silva                                                              *")
    print("*                                                                         Versão: 1.0   *")
    print("*                                                                          08/11/2023   *")
    print("*****************************************************************************************")

def escolha():
    print("Escolha uma opção:")
    print("(A)Continuar o cálculo")
    print("(B)Voltar ao menu principal")
    print("(C)Sair")

def opcao_a():
    binario = input("Escreve um número binário:\n")
    tamanho = len(binario)
    while not binario or not ((all(c in '01' for c in binario)) or (binario[0] == "-" and all(c in '01' for c in binario[1:]))):
        print("Por favor, digite um número válido!")
        binario = input("Escreve um número binário:\n")

    if binario[0] == "-":
        binario = binario[1:]
        decimal = "-"+binario_to_decimal(binario, tamanho-1)
        print("O número decimal correspondente é", decimal, "\n")
    else:
        tamanho = len(binario)  # atualizar o tamanho
        print("O número decimal correspondente é",
              binario_to_decimal(binario, tamanho), "\n")


def opcao_b():
    decimal = input("Escreve um número decimal:\n")
    while not decimal or not(decimal.isdigit() or (decimal[0] == "-" and decimal[1:].isdigit())):
        print("Por favor, digite um número válido!")
        decimal = input("Escreve um número decimal:\n")

    if int(decimal) > 0:
        decimal = int(decimal)
        print("O número binário correspondente é",
              decimal_to_binario(decimal), "\n")
    else:
        decimal = int(decimal)
        binario = "-"+decimal_to_binario(abs(decimal))
        print("O número binário correspondente é", binario, "\n")


def binario_to_decimal(binario, tamanho):
    result = 0
    for c in binario:
        c = int(c)
        result += c * 2 ** (tamanho - 1)
        tamanho -= 1
    return str(result).strip()


def decimal_to_binario(decimal):
    result = list()
    while decimal > 0:
        result.append(decimal % 2)
        decimal = decimal // 2
    result.reverse()
    n = 0
    # passar de list para int
    for numero in result:
        n = n * 10 + numero
    return str(n).strip()


# Passa o str para int. Se conseguir, retorna True, se não, retorna False
def ft_isdigit(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def check_option(opção):
    while opção.lower() != "a" and opção.lower() != "b" and opção.lower() != "c":
        print("Por favor, escolha uma opção válida!")
        print("Escolha uma opção:")
        print("(A)Continuar o cálculo")
        print("(B)Voltar ao menu principal")
        print("(C)Sair")
        opção = input()
    if opção.lower() == "a":
        return "a"
    elif opção.lower() == "b":
        return "b"
    elif opção.lower() == "c":
        return "c"


########################################### MAIN FUNCTION #########################################
while True:
    menu_principal()
    option = input("Escolha uma opção:\n(A)Binário para decimal\n(B)Decimal para binário\n(C)Sair\n")
    while option.lower() != "a" and option.lower() != "b" and option.lower() != "c":
        print("Por favor, escolha uma opção válida!")
        option = input("Escolha uma opção:\n(A)Binário para decimal\n(B)Decimal para binário\n(C)Sair\n")

    if option.lower() == "a":
        opcao_a()
        escolha()

        opção = input()
        while opção.lower() != "a" and opção.lower() != "b" and opção.lower() != "c":
            print("Por favor, escolha uma opção válida!")
            escolha()
            opção = input()

        while opção.lower() == "a":
            opcao_a()
            escolha()
            opção = input()
            opção = check_option(opção)

        if opção.lower() == "b":
            continue
        elif opção.lower() == "c":
            break

    if option.lower() == "b":
        opcao_b()
        escolha()
        opção = input()

        while opção.lower() != "a" and opção.lower() != "b" and opção.lower() != "c":
            print("Por favor, escolha uma opção válida!")
            escolha()
            opção = input()

        while opção.lower() == "a":
            opcao_b()
            escolha()
            opção = input()
            opção = check_option(opção)

        if opção.lower() == "b":
            continue
        elif opção.lower() == "c":
            break

    elif option.lower() == "c":
        break

print("Obrigado por calcular connosco!")