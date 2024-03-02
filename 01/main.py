from Cliente import Cliente

cliente = Cliente.cadastrar_cliente()

if cliente:
  nome_cliente = cliente.get_nome()
  endereco_cliente = cliente.get_endereco()
  cep_cliente = cliente.get_cep()
  cpf_cliente = cliente.get_cpf()
  print(f"Cliente cadastrado com sucesso!\nNome: {nome_cliente}\nEndereço: {endereco_cliente}\nCEP: {cep_cliente}\nCPF: {cpf_cliente}")

