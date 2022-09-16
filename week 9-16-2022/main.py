import re

def validHexCode(string):
    if(len(string) != 7):
        return False
    match = re.search(r'#[0-9a-fA-F]{6}', string)
    if match:
        return True
    else:
        return False

def is_prime(n):
  for i in range(2,n):
        if (n % i) == 0:
            return False
  return True

def nextPrime(value):
    if(is_prime(value)):
        return value
    return nextPrime(value+1)

print(nextPrime(10))