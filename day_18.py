import sys
import numpy as np
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  # print(f'Message from stdin: {line}')
  # break
print(txt)


pos = [0,0]
rows = []
for t in txt:
  # print(t)
  start = pos

  direction = t.split(" ")[0]
  nr = int(t.split(" ")[1])
  
  y_move = False
  x_move = False
  if direction == 'U':
    for r in range(start[1],start[1] - nr - 1, -1):
      rows.append([start[0],r])
      
  elif direction == 'D':
    for r in range(start[1], start[1] + nr + 1):
      rows.append([start[0],r])
      
  elif direction == 'R':
    for r in range(start[0], start[0] + nr + 1):
      rows.append([r,start[1]])
      
  elif direction == 'L':
    for r in range(start[0],start[0] - nr - 1,-1):
      rows.append([r,start[1]])

  pos = rows[-1]
  
max_row_dict = {}
min_row_dict = {}
max_col_dict = {}
min_col_dict = {}

for r in rows:
  x = r[0]
  y = r[1]
  
  if y in max_row_dict.keys():
    if x > max_row_dict[y]:
      max_row_dict[y] = x
  else:
    max_row_dict[y] = x
    
  if y in min_row_dict.keys():
    if x < min_row_dict[y]:
      min_row_dict[y] = x
  else:
    min_row_dict[y] = x

# print(max_row_dict)
# print(min_row_dict)

total = 0
for k, val in max_row_dict.items():
  nr_ones = max_row_dict[k]-min_row_dict[k]+1
  # print(nr_ones)
  total +=nr_ones
print(total)
