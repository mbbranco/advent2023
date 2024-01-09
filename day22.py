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

coords_left = [x.split("~")[0] for x in txt]
coords_right = [x.split("~")[1] for x in txt]

print(coords_left)
print(coords_right)
bricks_dict = {}
abc = [chr(i) for i in range(ord('a'),ord('z')+1)]

for i,c in enumerate(coords_left):
  left = coords_left[i].split(",")
  left = [int(l) for l in left]
  
  right = coords_right[i].split(",")
  right = [int(l) for l in right]

  bricks_dict[abc[i]] = [left,right]

print(bricks_dict)

max_x = max_y = max_z = 0
for k,val in bricks_dict.items():
  for v in val:
    x = v[0]
    y = v[1]
    z = v[2]
    max_x = max(x,max_x)
    max_y = max(y,max_y)
    max_z = max(z,max_z)

x_z_dict = {}
y_z_dict = {}
max_z = max_x = max_y = 0
for k,val in bricks_dict.items():
  start = val[0]
  finish = val[1]
  
  x = list(range(start[0],finish[0]+1))
  y = list(range(start[1],finish[1]+1))
  z = list(range(start[2],finish[2]+1))
  
  max_z = max(max(z),max_z)
  max_x = max(max(x),max_x)
  max_y = max(max(y),max_y)
  
  x_final = x
  y_final = y
  z_final = z
  if len(z)==1 and len(x)>1:
    z_final = z*len(x)
  elif len(x) == 1 and len(z)>1:
    x_final = x*len(z)
    
  x_z_dict[k] = list(zip(x_final,z_final))
  
  if len(z)==1 and len(y)>1:
    z_final = z*len(y)
  elif len(y) == 1 and len(z)>1:
    y_final = y*len(z)
    
  y_z_dict[k] = list(zip(y_final,z_final))
  
print(x_z_dict)
print(y_z_dict)
print(max_x,max_y,max_z)

matrix_xz = np.full([max_z+1,max_x+1],'.')
for letter,posi in x_z_dict.items():
  for k in posi:
    matrix_xz[k[1],k[0]] = letter

matrix_xz = np.flip(matrix_xz,0) # horizontal flip
for m in matrix_xz:
  print(''.join(m))
print()
matrix_yz = np.full([max_z+1,max_y+1],'.')
for letter,posi in y_z_dict.items():
  for k in posi:
    matrix_yz[k[1],k[0]] = letter

matrix_yz = np.flip(matrix_yz,0) # horizontal flip
for m in matrix_yz:
  print(''.join(m))

mask = []
for i,x in enumerate(matrix_xz):
  mask.append((x=='.').sum(0)!=3)
  
matrix_xz_clean = matrix_xz[mask]
print(matrix_xz_clean)

