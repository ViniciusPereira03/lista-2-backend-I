from Cpf import Cpf

cpf_input = input('Digite o CPF: ')
cpf = Cpf(cpf_input)

if cpf.validar():
  print('CPF válido.')
else:
  print('CPF inválido.')
