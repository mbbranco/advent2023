import sys
import numpy as np
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  

corr = txt[0].split(",")
# print(corr)

step_val = []
current_value = 0
for c in corr:
  # print(c)
  for char in c:
    ascii_val = ord(char)
    current_value += ascii_val
    current_value *= 17
    current_value = current_value % 256
  
  # print(current_value)
  step_val.append(current_value)
  current_value = 0

print(step_val)
print(sum(step_val))
