import sys
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  
print(txt)

hands = []
scores = []
for t in txt:
  hand = t.split(" ")
  cards = [h for h in hand[0]]
  hands.append(cards)
  scores.append(int(hand[1]))
  
print(hands)
print(scores)

for i,h in enumerate(hands):
  print(f'Hand: {h}')
  dif_cards = set(h)
  if len(dif_cards)==len(h):
    print("one of a kind")
  else:
    dict_cards = {}
    for d in dif_cards:
      dict_cards[d] = h.count(d)
  print(dict_cards)
