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

garden = []
for i,t in enumerate(txt):
  l = [x for x in t]
  if 'S' in l:
    j = l.index('S')
    start_x = i
    start_y = j
  garden.append(l)

# print(garden)
n_steps = 64
print(start_x,start_y)
max_y = len(garden)-1
max_x = len(garden[0])-1


def get_coords(x,y):
  n_coords = [max(0,x-1),y]
  e_coords = [x,min(y+1,max_y)]
  w_coords = [x,max(0,y-1)]
  s_coords = [min(x+1,max_x),y]
  
  coords = [n_coords,e_coords,w_coords,s_coords]
  # print(coords)
  valid_coords = []
  for c in coords:
    pos = garden[c[0]][c[1]]
    if pos != "#":
      valid_coords.append(c)
  return valid_coords

coords = get_coords(start_x,start_y)
# print(coords)
for i in range(1,n_steps):
  # print(f'Step: {i+1}')
  full_coords = []
  for c in coords:
    new_coords = get_coords(c[0],c[1])
    # print(new_coords)
    full_coords.extend(new_coords)

  uni_coords = [] 
  for f in full_coords:
    if f not in uni_coords:
      uni_coords.append(f)
  coords = uni_coords.copy()

  
  new_garden = [x[:] for x in garden]
  for c in full_coords:
    new_garden[c[0]][c[1]]= 'O'

  # print()
  # for g in new_garden:
    # print(''.join(g))
  

print(len(coords))
  
