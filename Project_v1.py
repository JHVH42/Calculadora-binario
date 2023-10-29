#################################### FUNÇÕES###########################################
def binario_to_decimal(binario, tamanho):
    result = 0
    for c in binario:
        c = int(c)
        result += c * 2 ** (tamanho - 1)
        tamanho -= 1
    print(result)


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

    while opção.lower() != "a" and not opção.lower() != "b":
        print("Por favor, escolha uma opção válida!")

    if opção.lower() == "a":
        return True
    elif opção.lower() == "b":
        return False


"""
def decimal_to_binario(decimal):
  ls = list()
  n = 0
  #Obter o expoente
  while 2**n <= decimal:
    n += 1
  #decimal -= 2**(n - 1)
  while True:
    result = decimal - 2**(n - 1)
    if result > 0:
      #result = 1
      ls.append(1)
    else:
      #result = 0
      ls.append(0)
  #ls.append(result)
  return ls
#binario = str(input("Escreve um número binario "))
#tamanho = len(decimal)
"""
################################### MAIN FUNCTION#########################################
while True:
    decimal = input("Escreve um número decimal:\n")
    if not (ft_isdigit(decimal) or (decimal[0] == "-" and ft_isdigit(decimal[1:]))):
        print("Por favor, digite um número válido!")
        continue
    elif int(decimal) > 0:
        decimal = int(decimal)
        print("O número binário correspondente é",
              decimal_to_binario(decimal), "\n")
    else:
        decimal = int(decimal)
        binario = "-"+decimal_to_binario(decimal)
        print("O número binário correspondente é", binario, "\n")

    print("Escolha uma opção:")
    print("(A)Continuar o cálculo")
    print("(B)Sair")
    opção = input()

    while opção.lower() != "a" and opção.lower() != "b":
        print("Por favor, escolha uma opção válida!")
        print("Escolha uma opção:")
        print("(A)Continuar o cálculo")
        print("(B)Sair")
        opção = input()
        continue
    if opção.lower() == "a":
        continue
    elif opção.lower() == "b":
        break

print("Obrigado por calcular connosco!")
