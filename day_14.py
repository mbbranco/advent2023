import sys
import numpy as np
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  
print(txt)

groups = []
new_group = []
# print(txt)
for t in txt:
  if t!="":
    t = [x for x in t]
    new_group.append(t)
  else:
    groups.append(new_group)
    new_group = []

groups.append(new_group)


# print(groups)

nr_cols = len(groups[0])
final_pos_dict = {}

for j in range(0,nr_cols):
  print(f'Col {j}')
  final_pos_dict[j] = []
  for i, row in enumerate(groups):
    ng = np.array(row)
    col = ng[:,j]
    col_reversed = list(col[::-1])
    # print(col_reversed)
    for k, z in enumerate(col_reversed):
      if z == 'O':
        remain = col_reversed[k:]
        # print(remain)
        if remain.count("#")==0:
          print('No More Rocks')
          nr_zeros = remain.count("O")
          final_pos_dict[j].append(nr_zeros-1)
        else:
          next_rock = remain.index("#")
          next_rock_inverted = len(remain) - 1 -  next_rock
          
          remain_next_rock = remain[0:next_rock]
          print('Rocks')
          nr_zeros = remain_next_rock.count("O")
          final_pos_dict[j].append(next_rock_inverted + nr_zeros)
          
          
  # print(final_pos_dict[j])
  
print(final_pos_dict)

final_pos_dict_v2 = {}
for k, val in final_pos_dict.items():
  for v in val:
    if v not in final_pos_dict_v2.keys():
      final_pos_dict_v2[v] = 1
    else:
      final_pos_dict_v2[v] += 1
    
print(final_pos_dict_v2)

total_sum = 0
for k, val in final_pos_dict_v2.items():
  print(nr_cols-k, val)
  total_sum+=(nr_cols-k)*val
  
print(total_sum)
  
  
      
