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
max_x = 0
max_y = 0
for t in txt:
  direction = t[0]
  nr = int(t.split(" ")[1])
  # print(direction,nr)
  # print(pos)
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

  range_v = list(zip(range_x,range_y))
  max_x = max(max(range_x),max_x)
  max_y = max(max(range_y),max_y)
  result.extend(range_v)
  pos = new_pos


finals = []
final = ["."]*(max_y+1)
for i in range(0,max_x+1):
  finals.append(final)
  
finals = np.array(finals)
for i in range(0,max_x+1):
  for j in range(0,max_y+1):
    pair = (i,j)
    if pair in result:
      finals[i,j] = "#"
      
print(finals)

nr_houses = 0
for k in finals:
  left = []
  for i,l in enumerate(k):
    if l == "#":
      left.append(i)
  nr_houses += max(left)-min(left)+1

print(nr_houses)
