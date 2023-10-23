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
  #passar de list para int
  for numero in result:
    n = n * 10 + numero
  return n

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

#decimal = input("Escreve um número decimal ")
while True:
  decimal = input("Escreve um número decimal ")
  if not decimal.isdigit() or int(decimal) < 0:
    print("Erro!!! Por favor, digite um número válido!")
    continue
  else:
    decimal = int(decimal)
    print(decimal_to_binario(decimal))
    continue