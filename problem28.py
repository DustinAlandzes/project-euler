def spiral_diag_sum(n):
  """
  returns sum of diagonals of an n*n grid
  
  :param: n - size of n*n grid
  """
  if n < 1 or n % 2 == 0:
    raise ValueError(n)
  
  # grid starting with 1
  numbers = [1]
  
  while len(numbers) < (2*n - 1):
    increment += 2
    for p in range(4):
      numbers.append(numbers[-1] + increment)     
  return sum(numbers)

print(spiral_diag_sum(1001))
