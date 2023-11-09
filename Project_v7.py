import os
#################################### MENUS ###########################################
def menu_principal():
    print("*****************************************************************************************")
    print("*   Benvido ao nosso programa de cálculo!                                               *")
    print("*                                                                                       *")
    print("*   A nossa calculadora é capaz de converter números binários em decimais e vice-versa! *")
    print("*   Esperamos que goste!                                                                *")
    print("*                                                                                       *")
    print("*          \033[1;31m!!! O nosso programa só é capz de calcular com números inteiros !!! \033[0m         *")
    print("*                                                                                       *")
    print("*****************************************************************************************")
    print("*                                                                                       *")
    print("*   Realizado por: Artur Alves e Jinhua Chen                                            *")
    print("*   Turma: 12ºCE                                                                        *")
    print("*   Escola: Colégio Vasco da Gama                                                       *")
    print("*   Disciplina: AIB                                                                     *")
    print("*   Professor: Pedro Silva                                                              *")
    print("*                                                                         Versão: 1.0   *")
    print("*                                                                          10/11/2023   *")
    print("*****************************************************************************************")

def menu_opcao_a():
    print("*****************************************************************************************")
    print("*                                                                                       *")
    print("*                        Converter binário para decimal                                 *")
    print("*                                                                                       *")
    print("*****************************************************************************************")


def menu_opcao_b():
    print("*****************************************************************************************")
    print("*                                                                                       *")
    print("*                        Converter decimal para binário                                 *")
    print("*                                                                                       *")
    print("*****************************************************************************************")


#################################### FUNÇÕES DE VERIFICAÇÕES ###########################################
def opcao_a():
    binario = input("Escreve um número binário:\n")
    tamanho = len(binario)
    while not binario or not ((all(c in '01' for c in binario)) or (binario[0] == "-" and all(c in '01' for c in binario[1:]))):
        printRed("Por favor, digite um número válido!")
        binario = input("Escreve um número binário:\n")

    if binario[0] == "-":
        binario = binario[1:]
        decimal = "-"+binario_to_decimal(binario, tamanho-1)
        print("O número decimal correspondente é", decimal, "\n")
    else:
        tamanho = len(binario)  # atualizar o tamanho
        print("O número decimal correspondente é", binario_to_decimal(binario, tamanho), "\n")


def opcao_b():
    decimal = input("Escreve um número decimal:\n")
    while not decimal or not(decimal.isdigit() or (decimal[0] == "-" and decimal[1:].isdigit())):
        printRed("Por favor, digite um número válido!")
        decimal = input("Escreve um número decimal:\n")

    if int(decimal) > 0:
        decimal = int(decimal)
        print("O número binário correspondente é",
              decimal_to_binario(decimal), "\n")
    else:
        decimal = int(decimal)
        binario = "-"+decimal_to_binario(abs(decimal))
        print("O número binário correspondente é", binario, "\n")


def escolha():
    print("Escolha uma opção:")
    print("[A] Continuar o cálculo")
    print("[B] Voltar ao menu principal")
    print("[C] Sair")


def check_option(opção):
    while opção.lower() != "a" and opção.lower() != "b" and opção.lower() != "c":
        printRed("Por favor, escolha uma opção válida!")
        escolha()
        opção = input()
    if opção.lower() == "a":
        return "a"
    elif opção.lower() == "b":
        return "b"
    elif opção.lower() == "c":
        return "c"


#################################### FUNÇÕES DE CÁLCULOS ###########################################
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


#################################### FUNÇÕES DE PRINTS COM COR ###########################################
def printRed(text):
    redText = "\033[91m" + text + "\033[00m"
    print(redText)


########################################### MAIN FUNCTION #########################################
while True:
    menu_principal()
    option = input("Escolha uma opção:\n[A] Binário para decimal\n[B] Decimal para binário\n[C] Sair\n")
    while option.lower() != "a" and option.lower() != "b" and option.lower() != "c":
        printRed("Por favor, escolha uma opção válida!")
        option = input("Escolha uma opção:\n[A] Binário para decimal\n[B] Decimal para binário\n[C] Sair\n")

    if option.lower() == "a":
        os.system('cls')
        menu_opcao_a()
        opcao_a()
        escolha()

        opção = input()
        while opção.lower() != "a" and opção.lower() != "b" and opção.lower() != "c":
            printRed("Por favor, escolha uma opção válida!")
            escolha()
            opção = input()

        while opção.lower() == "a":
            os.system('cls')
            menu_opcao_a()
            opcao_a()
            escolha()
            opção = input()
            opção = check_option(opção)

        if opção.lower() == "b":
            os.system('cls')
            continue
        elif opção.lower() == "c":
            os.system('cls')
            break

    if option.lower() == "b":
        os.system('cls')
        menu_opcao_b()
        opcao_b()
        escolha()
        opção = input()

        while opção.lower() != "a" and opção.lower() != "b" and opção.lower() != "c":
            printRed("Por favor, escolha uma opção válida!")
            escolha()
            opção = input()

        while opção.lower() == "a":
            os.system('cls')
            menu_opcao_b()
            opcao_b()
            escolha()
            opção = input()
            opção = check_option(opção)

        if opção.lower() == "b":
            os.system('cls')
            continue
        elif opção.lower() == "c":
            os.system('cls')
            break

    elif option.lower() == "c":
        os.system('cls')
        break

print("Obrigado por calcular connosco!")