import sys

def strReverse(s):
  result = ''
  for i in s:
    result = i + result
  return result

if __name__ == '__main__':
  s = sys.argv[1]
  print(strReverse(s))