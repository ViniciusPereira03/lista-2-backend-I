import math

class Primos:

  def __init__(self, num_1: int, num_2: int):
    self._num_1 = num_1
    self._num_2 = num_2

  def set_num_1(self, num_1):
      self._num_1 = num_1

  def set_num_2(self, num_2):
      self._num_2 = num_2

  def get_num_1(self):
    return self._num_1
  
  def get_num_2(self):
    return self._num_2

  @staticmethod
  def ehPrimo(num):
    for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
        return False
    return True

  @staticmethod
  def conta_primos(num1, num2):
    total_primos = 0
    for i in range(num1, num2+1):
      if Primos.ehPrimo(i):
        total_primos += 1
    
    return total_primos

