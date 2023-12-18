import sys
import numpy as np

# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  # print(f'Message from stdin: {line}')
  # break
# print(txt)

characters = []
for t in txt:
  chars = [c for c in t]
  characters.append(chars)
matriz = np.array(characters)

# print(matriz)
nr_rows,nr_cols = matriz.shape

positions = []
positions_list = []
numbers_list = []
char = ""
for i in range(0,nr_rows):
  for j in range(0,nr_cols):
    c = matriz[i][j]
    if c.isdigit():
      char += c
      positions.append([i,j])
    else:
      if len(positions)>0:
        positions_list.append(positions)
        numbers_list.append(char)
        char = ''
        positions = []
      
# print(positions_list)
# print(numbers_list)

max_len = len(txt)-1
numbers_part = []
potential_gears_dict = {}
for i,pos in enumerate(positions_list):
  nr = numbers_list[i]
  row = pos[0][0]
  ini = pos[0][1]
  fim = pos[-1][1]
  
  min_row = max(row-1,0)
  max_row = min(row+1,max_len)
  min_col = max(ini-1,0)
  max_col = min(fim+1,max_len)

  for i in range(min_row,max_row+1):
    for j in range(min_col,max_col+1):
      val = txt[i][j]
      if not val.isdigit() and val!=".":
        # print(val)
        numbers_part.append(int(nr))
        pos_txt = str(i)+"_"+str(j)
        if pos_txt in potential_gears_dict.keys():
          potential_gears_dict[pos_txt].append(int(nr))
        else:
          potential_gears_dict[pos_txt] = [int(nr)]
        
total_sum = 0 
for pos, val in potential_gears_dict.items():
  if len(val)==2:
    total_sum += val[0] * val[1]
print(total_sum)
