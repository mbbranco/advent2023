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

total_sum = 0
for seq in sequence:
  reached_bottom = False
  levels = []
  while reached_bottom == False:
    levels.append(seq)
    new_seq = get_diffs(seq)
    if sum(new_seq) == 0:
      reached_bottom = True
    seq = new_seq

  phs = []
  cumsum = 0
  for j in range(len(levels)-1,-1,-1):
    cl = levels[j][-1]
    cumsum +=cl
    phs.append(cumsum)
  
  # print(f'seq: {phs} | cumsum: {sum(phs)}')
  total_sum += phs[-1]
  # total_sum += 
print(total_sum)
