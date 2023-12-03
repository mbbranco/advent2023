import sys

# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  # print(f'Message from stdin: {line}')
  # break
print(txt)

positions = []
positions_list = []
numbers_list = []
char = ""
i = 0
for line in txt:
  j = 0
  for c in line:
    if c.isdigit():
      char += c
      positions.append([i,j])
    else:
      if len(positions)>0:
        positions_list.append(positions)
        numbers_list.append(char)
        char = ''
        positions = []
    j+=1
  i+=1
      
# print(positions_list)
# print(numbers_list)

max_len = len(txt)-1
numbers_part = []
for i,pos in enumerate(positions_list):
  # nr,list_pos in positions_dict.items():
  # print(nr)
  nr = numbers_list[i]
  row = pos[0][0]
  ini = pos[0][1]
  fim = pos[-1][1]
  
  min_row = max(row-1,0)
  max_row = min(row+1,max_len)
  min_col = max(ini-1,0)
  max_col = min(fim+1,max_len)
  # print(min_row,max_row)
  # print(min_col,max_col)
  for i in range(min_row,max_row+1):
    for j in range(min_col,max_col+1):
      val = txt[i][j]
      if not val.isdigit() and val!=".":
        # print(val)
        numbers_part.append(int(nr))
        

# print(numbers_part)
# print(list(positions_dict.keys()))
print(sum(numbers_part))

# for t in check_pos:
#   print(txt[t[0]][t[1]])
