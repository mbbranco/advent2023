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


def check_sym(type_c):
  # check horizontal
  sym_result = {}
  for id_group, g in enumerate(groups):
    print(f'\n\n{id_group}')
    ng = np.array(g)
    if type_c == 'horizontal':
      #nr rows
      nr_final = len(ng)
      t_ = 'Linha'
    else:
      #nr cols
      nr_final = len(ng[0])
      t_ = 'Coluna'
      
    for i in range(0,nr_final-1):
      # print(f'\n {t_} Atual {i}')
      left_window = range(0,i+1)
      right_window = range(i+1,nr_final)
      # print(list(left_window))
      # print(list(right_window))
      
      max_len = min(len(left_window),len(right_window))
      
      left_r = range(i+1-max_len,i+1)
      right_r = range(i+1,i+1+max_len)
      if type_c == 'horizontal':
        left_side = ng[left_r,:]
        right_side = ng[right_r,:]
        right_side_reversed =  np.flipud(right_side)
      else:
        left_side = ng[:,left_r]
        right_side = ng[:,right_r]
        right_side_reversed =  np.fliplr(right_side)
    

      # print(f'Comparar {t_} {list(left_r)} vs {list(right_r)}')

      left_side_10 = np.char.replace(left_side, '#', '1')
      left_side_10 = np.char.replace(left_side_10, '.', '0')
      left_side_10 = left_side_10.astype(int)
      
      right_side_rev_10 = np.char.replace(right_side_reversed, '#', '1')
      right_side_rev_10 = np.char.replace(right_side_rev_10, '.', '0')
      right_side_rev_10 = right_side_rev_10.astype(int)
      
      dif = left_side_10 - right_side_rev_10
      # print(left_side_10)
      # print(right_side_rev_10)
      # print(dif)
      nr_lin_dif = 0
      nr_lin_ok = 0
      for d in dif:
        nr_ones = sum(d==1)
        nr_zeros = sum(d==0)
        
        if nr_zeros == len(d):
          nr_lin_ok+=1
        elif nr_ones==1 and nr_zeros==len(d)-1:
          nr_lin_dif +=1
        else:
          break
      
      if nr_lin_dif == 1 and nr_lin_ok == len(dif)-1:
        # print('Smudge')
        print(dif)
        sym_result[id_group] = len(left_window)
        break
      elif nr_lin_ok == len(dif):
        # print('Symmetric')
        sym_result[id_group] = len(left_window)

        
            
  return sym_result
    

horiz_sym = check_sym('horizontal')
vert_sym = check_sym('vertical')
print(horiz_sym)
print(vert_sym)


mult_horiz = [100*x for x in horiz_sym.values()]
final_result = sum(mult_horiz)+sum(vert_sym.values())
print(final_result)
