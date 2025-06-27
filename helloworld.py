print("hello_world")

def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)
print("hello_world")

import math
def median(input):
  x = len(input)
  y = math.floor(x/2)
  if x % 2 == 0:
    return (input[y] + input[y+1])/2
  else:
    return input[y]