import math

class Operacoes:
  @staticmethod
  def soma(num1, num2):
    return num1 + num2
  
  @staticmethod
  def subtracao(num1, num2):
    return num1 - num2
  
  @staticmethod
  def multiplicacao(num1, num2):
    return num1 * num2
  
  @staticmethod
  def radiciacao(num1, num2):
    return math.pow(num1, 1/num2)

  @staticmethod
  def fatorial(num):
    if num == 0 or num == 1:
      return 1
    else:
      return num * Operacoes.fatorial(num - 1)

  