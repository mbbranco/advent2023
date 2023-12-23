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
result = [(0,0)]
dict_row = {}
for t in txt:
  direction = t[0]
  nr = int(t.split(" ")[1])
  print(direction,nr)
  print(pos)
  if direction == 'R':
    new_pos = [pos[0],pos[1]+nr]
    range_x = [pos[0]]*(nr+1)
    range_y = list(range(pos[1],pos[1]+nr+1))
  elif direction == 'D':
    new_pos = [pos[0]+nr,pos[1]]
    range_y = [pos[1]]*(nr+1)
    range_x = list(range(pos[0],pos[0]+nr+1))
  elif direction == 'U':
    new_pos = [pos[0]-nr,pos[1]]
    range_y = [pos[1]]*(nr+1)
    range_x = list(range(pos[0]-nr,pos[0]+1))
  elif direction == 'L':
    new_pos = [pos[0],pos[1]-nr]
    range_x = [pos[0]]*(nr+1)
    range_y = list(range(pos[1]-nr,pos[1]+1))


  left = range_y[0]
  right = range_y[-1]
  for x in range_x:
    if x in dict_row.keys():
      val = dict_row[x]
      dict_row[x] = (min(val[0],left),max(val[1],right))
    else:
      dict_row[x] = (left,right)

  # result.extend(range_v)
  pos = new_pos
print(dict_row)
# print(result)
# print(sorted(result))

nr_houses = 0
for k, val in dict_row.items():
  dif = val[1]-val[0]+1
  print(dif)
  nr_houses+=abs(dif)

print(nr_houses)
