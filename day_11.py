import sys
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  
print(txt)

maps = []
for t in txt:
  maps.append([i for i in t])

print(f'N Rows: {len(maps)} | N Cols: {len(maps[0])}')

empty_rows = []
# check rows
for i,row in enumerate(maps):
  if row.count("#") == 0:
    empty_rows.append(i)

print(empty_rows)
  
empty_cols = []
# check columns
n_columns = len(maps[0])
for j in range(0,n_columns):
  not_found = True
  for i,row in enumerate(maps):
    if maps[i][j]=="#":
      not_found = False
      break
  if not_found:
    empty_cols.append(j)

print(empty_cols)

# expand rows
new_pos = 0
for pos in empty_rows:
  final_pos = pos + new_pos
  list_add = ["."]*n_columns
  maps.insert(final_pos,list_add)
  new_pos+=1


# expand cols
new_pos = 0
for pos in empty_cols:
  final_pos = pos + new_pos
  for i, row in enumerate(maps):
    maps[i].insert(final_pos,".")
  new_pos+=1


print(f'N Rows: {len(maps)} | N Cols: {len(maps[0])}')

# number galaxies
n_columns = len(maps[0])
counter = 1
counter_dict = {}
for i,row in enumerate(maps):
  for j,val in enumerate(row):
    if val=="#":
      maps[i][j] = counter
      counter_dict[counter] = [i,j]
      counter+=1
      
# print(maps)
# print(counter_dict)

combi = []
for i in range(1,counter):
  for j in range(i+1,counter):
    combi.append([i,j])
    
combi_dict = {}
n_steps_needed = 0
for c in combi:
  gal_a = c[0]
  gal_b = c[1]
  combi = str(gal_a)+" => "+str(gal_b)
  coords_a = counter_dict[gal_a]
  coords_b = counter_dict[gal_b]
  
  dif_x = abs(coords_a[0] - coords_b[0])
  dif_y = abs(coords_a[1] - coords_b[1])
  n_steps_needed = dif_x + dif_y
  combi_dict[combi] = n_steps_needed

# print(combi_dict)
print(sum(combi_dict.values()))
