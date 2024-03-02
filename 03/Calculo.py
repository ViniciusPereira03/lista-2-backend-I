from typing import Tuple

class Calculo:
  
  @staticmethod
  def calcular(*args):

    print(isinstance(args[0], list))

    if len(args) == 1 and isinstance(args[0], (float, int)):
      return f"Área do círculo: {3.14 * (args[0] ** 2)}"
    
    elif len(args) == 2 and all(isinstance(arg, (float, int)) for arg in args):
      return f"Área do quadrado: {args[0] * args[1]}"
    
    elif len(args) == 3 and all(isinstance(arg, int) for arg in args):
      return f"Perímetro do triângulo: {sum(args)}"
    
    elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], float):
      return f"Área do triângulo: {0.5 * args[0] * args[1]}"
   
    elif len(args) == 3 and isinstance(args[0], list) and isinstance(args[1], list) and isinstance(args[2], list) and len(args[0]) == 2 and len(args[1]) == 2 and len(args[2]) == 2:
      x1, y1 = args[0]
      x2, y2 = args[1]
      x3, y3 = args[2]

      area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
      return f"Área do triângulo  (coordenadas cartesianas): {area}"

    else:
      return "Uso incorreto"
      