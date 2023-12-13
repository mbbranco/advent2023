import sys
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  
print(txt)
sequence = []
for i in txt:
  seq = i.split(" ")
  sequence.append([int(s) for s in seq])
# print(sequence)

def get_diffs(seq):
  diffs = []
  for i in range(0,len(seq)-1):
    d = seq[i+1]-seq[i]
    diffs.append(d)
  return diffs

levels_all = []
for seq in sequence:
  # print(seq)
  reached_bottom = False
  levels = []
  while reached_bottom == False:
    levels.append(seq[-1])
    new_seq = get_diffs(seq)
    # print(new_seq)
    if new_seq.count(0) == len(new_seq):
      reached_bottom = True
    seq = new_seq
    
  print(f'Levels: {levels}\n')
  levels_all.append(levels)

total = 0
for lev in levels_all:
  subtotal = 0
  for i in range(len(lev)-1,-1,-1):
    subtotal += lev[i]
  total+=subtotal
  
print(total)
