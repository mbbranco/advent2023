import sys
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  
instructions = [t for t in txt[0]]
print(instructions)


dict_nodes = {}
for t in txt[2:]:
  node, p = t.split(" = ")
  l,r = p.split(", ")
  dict_nodes[node] = [l[1:],r[:-1]]
  
print(dict_nodes)

start = 'AAA'
finish = ''
n_steps = 0 
i = 0
while finish !='ZZZ':
  instr = instructions[i]
  if instr =='R':
    finish = dict_nodes[start][1]
  else:
    finish = dict_nodes[start][0]
  
  # print(finish)
  n_steps+=1
  start = finish

  if i+1==len(instructions):
    i = 0
  else:
    i += 1

print(n_steps)
