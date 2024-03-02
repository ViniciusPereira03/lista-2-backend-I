from Primos import Primos

primos_instance = Primos(0, 0)

while True:
  try:
    num1 = int(input('Informe um número: '))
    if num1 > 0 :
      primos_instance.set_num_1(num1)
      break
    else:
      print('Erro: Informe um número positivo!')
  except ValueError:
    print('Erro: Informe somente números inteiros!')


while True:
  try:
    num2 = int(input('Informe um número: '))
    if num2 > 0 :
      if num2 > num1:
        primos_instance.set_num_2(num2)
        break
      else:
        print('Erro: Informe um número maior que o primeiro!')
    else:
      print('Erro: Informe um número positivo!')
  except ValueError:
    print('Erro: Informe somente números inteiros!')

num_1 = primos_instance.get_num_1()
num_2 = primos_instance.get_num_2()

total_primos = primos_instance.conta_primos(num_1, num_2)

print(f"Números: {num_1} e {num_2}")
print(f"Total de primos: {total_primos}")
