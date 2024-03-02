import re

class Cpf:
  def __init__(self, cpf):
    self._cpf = cpf

  def validar(self):
    cpf_numerico = re.sub(r'\D', '', self._cpf)

    if len(cpf_numerico) != 11:
      return False

    if cpf_numerico == cpf_numerico[0] * 11:
      return False

    if re.match(r'^(\d)\1+$', cpf_numerico):
      return False

    soma_1 = sum(int(cpf_numerico[i]) * (10 - i) for i in range(9)) % 11
    digito_1 = 0 if soma_1 < 2 else 11 - soma_1

    soma_2 = sum(int(cpf_numerico[i]) * (11 - i) for i in range(10)) % 11
    digito_2 = 0 if soma_2 < 2 else 11 - soma_2

    return int(cpf_numerico[9]) == digito_1 and int(cpf_numerico[10]) == digito_2
