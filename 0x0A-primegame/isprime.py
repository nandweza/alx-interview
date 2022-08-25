#!/usr/bin/python3

def isprimeNumber(n):
  """Checks if a given num n is a prime number"""
  for i in range(len(2, int(n ** 0.5) + 1)):
    if not n % i:
      return False
  return True
  
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(isprimeNumber(a))