import sys

# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  # print(f'Message from stdin: {line}')
  # break
print(txt)

wins = []
cards = []
for c in txt:
  nr = c.split(": ")[0]
  rest = c.split(": ")[1]
  
  win = rest.split(" | ")[0]
  card = rest.split(" | ")[1]
  
  card = card.split(" ")
  card = [int(c) for c in card if c!=""]
  
  win = win.split(" ")
  win = [int(c) for c in win if c!=""]

  cards.append(card)
  wins.append(win)
    
# print(wins)
# print(cards)
# print()
nr_matches = 0
total_points= []
for i,current_card in enumerate(cards):
  current_win = wins[i]
  # print(current_win)
  for current_val in current_card:
    # print(current_val)
    if current_val in current_win:
      nr_matches+=1
  # print()
  # print(nr_matches)
  if nr_matches == 1:
    total_points.append(1)
  elif nr_matches == 0:
    total_points.append(0)
  else:
    total_points.append(2**(nr_matches-1))
  nr_matches = 0

print(total_points)
print(sum(total_points))
