import re

class Cliente:
    def __init__(self, nome: str, endereco: str, cep: str, cpf: str):
      self._nome = nome
      self._endereco = endereco
      self._cep = cep
      self._cpf = cpf

    # Métodos de acesso
    def get_nome(self):
      return self._nome

    def get_endereco(self):
      return self._endereco

    def get_cep(self):
      return self._cep

    def get_cpf(self):
      return self._cpf

    @staticmethod
    def validar_cpf(cpf):
      regex_cpf = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

      if not regex_cpf.match(cpf):
        return False

      if cpf == cpf[0] * 11:
        return False

      cpf_numerico = re.sub(r'\D', '', cpf)

      if re.match(r'^(\d)\1+$', cpf_numerico):
        return False

      if len(cpf_numerico) != 11:
        return False

      soma_1 = sum(int(cpf_numerico[i]) * (10 - i) for i in range(9)) % 11
      digito_1 = 0 if soma_1 < 2 else 11 - soma_1

      soma_2 = sum(int(cpf_numerico[i]) * (11 - i) for i in range(10)) % 11
      digito_2 = 0 if soma_2 < 2 else 11 - soma_2

      return int(cpf_numerico[9]) == digito_1 and int(cpf_numerico[10]) == digito_2

    @staticmethod
    def validar_formato_cep(cep):
      regex_cep = re.compile(r'^\d{5}\-\d{3}$')

      if not regex_cep.match(cep):
        return False
        
      return True

    @staticmethod
    def cadastrar_cliente():
      nome = input("Digite o nome do cliente: ")
      endereco = input("Digite o endereço do cliente: ")
      cep = input("Digite o CEP do cliente: ")
      cpf = input("Digite o CPF do cliente (Informe o valor com mascara): ")

      if not Cliente.validar_formato_cep(cep):
        print("CEP inválido.")
        return None

      if not Cliente.validar_cpf(cpf):
        print("CPF inválido.")
        return None

      novo_cliente = Cliente(nome, endereco, cep, cpf)
      return novo_cliente
