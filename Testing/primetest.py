import math

def is_prime(n):
  #Números menores que 2 não são primos
  if n < 2:
    return False
  
  for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
      return False
  
  #Se não forem encontrados outros divisores, retorna True
  return True
