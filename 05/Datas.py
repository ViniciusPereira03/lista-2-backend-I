from datetime import datetime

class Datas:
  def __init__(self, data1, data2):
    self._data1 = datetime.strptime(data1, '%Y-%m-%d')
    self._data2 = datetime.strptime(data2, '%Y-%m-%d')

  def diferenca(self):
    diferenca = self._data2 - self._data1
    return diferenca.days
