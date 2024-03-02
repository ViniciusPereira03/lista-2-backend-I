from Datas import Datas

data1 = input("Informe a primeira data (formato YYYY-MM-DD): ")
data2 = input("Informe a segunda data (formato YYYY-MM-DD): ")

datas = Datas(data1, data2)
diferenca = datas.diferenca()

print(f"A diferença em dias das datas é: {diferenca} dia(s)")
