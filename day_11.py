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

# check rows
empty_rows = []
for i,row in enumerate(maps):
  if row.count("#") == 0:
    empty_rows.append(i)

print(empty_rows)
  
# check columns
empty_cols = []
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

size_expand = 1000000-1
new_coords = {}
for k,val in counter_dict.items():
  counter_cols = 0
  for i in empty_cols:
    if val[1]>=i:
      counter_cols+=size_expand
    
  counter_rows = 0
  for j in empty_rows:
    if val[0]>=j:
      counter_rows+=size_expand
      
  new_coords[k] = [val[0]+counter_rows,val[1]+counter_cols]

combi_dict = {}
n_steps_needed = 0
for c in combi:
  gal_a = c[0]
  gal_b = c[1]
  combi = str(gal_a)+" => "+str(gal_b)
  coords_a = new_coords[gal_a]
  coords_b = new_coords[gal_b]
  
  dif_x = abs(coords_a[0] - coords_b[0])
  dif_y = abs(coords_a[1] - coords_b[1])
  n_steps_needed = dif_x + dif_y
  combi_dict[combi] = n_steps_needed
# print(combi_dict)
print(sum(combi_dict.values()))
