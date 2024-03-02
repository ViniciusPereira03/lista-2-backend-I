from Operacoes import Operacoes

def get():
  while True:
    try:
      num = float(input("Digite um número: "))
      return num
    except ValueError:
      print("Por favor, digite um número válido.")

num1 = get()
num2 = get()

soma = Operacoes.soma(num1, num2)
subtracao = Operacoes.subtracao(num1, num2)
multiplicacao = Operacoes.multiplicacao(num1, num2)
radiciacao = Operacoes.radiciacao(num1, num2)
fatorial1 = Operacoes.fatorial(num1)
fatorial2 = Operacoes.fatorial(num2)

print(f"Soma: {soma}")
print(f"Subtracao: {subtracao}")
print(f"Multiplicacao: {multiplicacao}")
print(f"Radiciacao: {radiciacao}")
print(f"Fatorial num 1: {fatorial1}")
print(f"Fatorial num 2: {fatorial2}")
