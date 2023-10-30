#################################### FUNÇÕES###########################################
def menu_principal():
    print("Benvido ao nosso programa de cálculo!")

def so_para_opcao_a():
    binario = input("Escreve um número binário:\n")
    tamanho = len(binario)
    while not ((ft_isdigit(binario) and all(c in '01' for c in binario)) or (binario[0] == "-" and all(c in '01' for c in binario[1:]))):
      print("Por favor, digite um número válido!")
      binario = input("Escreve um número binário:\n")
      continue
    
    if binario[0] == "-":
      binario = binario[1:]
      decimal = "-"+binario_to_decimal(binario, tamanho-1)
      print("O número decimal correspondente é", decimal, "\n")
    else:
      print("O número decimal correspondente é", binario_to_decimal(binario, tamanho), "\n")


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

def ft_escolha_uma_opção():
    print("Escolha uma opção:")
    print("(A)Continuar o cálculo")
    print("(B)Sair")
    opção = input()

    while opção.lower() != "a" and opção.lower() != "b":
        print("Por favor, escolha uma opção válida!")

    if opção.lower() == "a":
        return True
    elif opção.lower() == "b":
        return False

###########################################MAIN FUNCTION#########################################
while True:
    menu_principal()
    option = input("Escolha uma opção:\n(A)Binário para decimal\n(B)Decimal para binário\n")
    while option.lower() != "a" and option.lower() != "b":
        print("Por favor, escolha uma opção válida!")
        option = input("Escolha uma opção:\n(A)Binário para decimal\n(B)Decimal para binário\n")
        continue
    if option.lower() == "a":
          binario = input("Escreve um número binário:\n")
          tamanho = len(binario)
          while not ((ft_isdigit(binario) and all(c in '01' for c in binario)) or (binario[0] == "-" and all(c in '01' for c in binario[1:]))):
               print("Por favor, digite um número válido!")
               binario = input("Escreve um número binário:\n")
               continue
          
          if binario[0] == "-":
                binario = binario[1:]
                decimal = "-"+binario_to_decimal(binario, tamanho-1)
                print("O número decimal correspondente é", decimal, "\n")
          else:
                print("O número decimal correspondente é", binario_to_decimal(binario, tamanho), "\n")

    elif option.lower() == "b":
        decimal = input("Escreve um número decimal:\n")
        if not (ft_isdigit(decimal) or (decimal[0] == "-" and ft_isdigit(decimal[1:]))):
             print("Por favor, digite um número válido!")
             continue
        elif int(decimal) > 0:
             decimal = int(decimal)
             print("O número binário correspondente é",decimal_to_binario(decimal), "\n")
        else:
             decimal = int(decimal)
             binario = "-"+decimal_to_binario(abs(decimal))
             print("O número binário correspondente é", binario, "\n")

    print("Escolha uma opção:")
    print("(A)Continuar o cálculo")
    print("(B)Voltar ao menu principal")
    print("(C)Sair")
    opção = input()

    while opção.lower() != "a" and opção.lower() != "b" and opção.lower() != "c":
        print("Por favor, escolha uma opção válida!")
        print("Escolha uma opção:")
        print("(A)Continuar o cálculo")
        print("(B)Voltar ao menu principal")
        print("(C)Sair")
        opção = input()
        continue
    if opção.lower() == "a":
        so_para_opcao_a()
    elif opção.lower() == "b":
        continue
    elif opção.lower() == "c":
        break

print("Obrigado por calcular connosco!")