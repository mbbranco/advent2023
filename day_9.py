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
  reached_bottom = False
  total_sum = 0
  levels = []
  while reached_bottom == False:
    levels.append(seq[-1])
    new_seq = get_diffs(seq)

    if sum(new_seq) == 0:
      reached_bottom = True
    seq = new_seq

    
  print(f'Levels: {levels}\n')
  levels_all.append(sum(levels))

print(levels_all)
print(sum(levels_all))
