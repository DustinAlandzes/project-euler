"""
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

import math

def is_prime(num):
  # type(int) -> bool
  """
  returns primality of num
  """
  if num < 2:
    return False
  if num == 2:
    return True

  # 3 - sqrt(num)
  for factor in range(3, int(math.sqrt(num)), 2):
    # not prime if num evenly divided by factor
    if num % factor == 0:
      return False
  
  return True


def equation(a, b, n):
  # type: (int, int, int) -> int
  """
  n^2 + an + b, 
  where |a| < 1000 and |b| ≤ 1000
  """
  return n**2 + a*n + b


def number_of_primes(a, b):
  # type: (int, int)
  """
  returns number of primes 
  """
  number_of_primes = 0

  while True:
    if is_prime(equation(a, b, number_of_primes)): 
      number_of_primes += 1
    else:
      break

  return number_of_primes


if __name__ == "__main__":
  best = 0
  besta = 0
  bestb = 0
  for a in range(1001):
    for b in range(1001):
      num_primes = number_of_primes(a, b)
      #print(a, b, num_primes)
      if num_primes > best:
        best = num_primes
        besta, bestb = a, b
  print(a * b, a, b)
