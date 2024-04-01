import sys

def doesItBellongToFibonacci(n):
  if (n == 0):
    return True
  if (n == 1):
    return True
  
  a = 0
  b = 1
  c = 1
  while(c < n):
    c = a + b
    a = b
    b = c
  
  if (c == n):
    return True
  else:
    return False

if __name__ == '__main__':
  n = int(sys.argv[1])
  print(doesItBellongToFibonacci(n))