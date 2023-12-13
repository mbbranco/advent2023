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
print(maps)

directions = {"|":[(0,-1),(0,1)], "-":[(1,0),(-1,0)],"L":[(0,-1),(1,0)],"J":((0,-1),(-1,0)),
"7":[(0,1),(-1,0)], "F":[(0,1),(-1,0)]}
