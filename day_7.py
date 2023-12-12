import sys
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  
print(txt)

hands_bids = {}
hands = []
scores = []
for t in txt:
  hand = t.split(" ")
  cards = [h for h in hand[0]]
  # hands.append(cards)
  # scores.append(int(hand[1]))
  hands_bids[hand[0]] = int(hand[1])
  
# print(hands)
# print(scores)
print(hands_bids)

rankings = []
dict_rankings = {}
for i in range(0,7):
  dict_rankings[i] = []
  
for i,h in enumerate(hands_bids.keys()):
  hand = [x for x in h]
  # print(f'\nHand: {hand}')
  dif_cards = set(hand)
  
  dict_repet = {}
  for j in range(1,6):
    dict_repet[j] = 0

  for d in dif_cards:
    contar = hand.count(d)
    dict_repet[contar] += 1

  rank = 6
  if dict_repet[5] == 1:
    # print()
    rank = rank
  elif dict_repet[4] == 1:
    # print('four of  a  kind')
    rank -= 1
  elif dict_repet[3] == 1 and dict_repet[2] == 1:
    # print('full house')
    rank -= 2
  elif dict_repet[3] == 1 and dict_repet[2] == 0:
    # print('three of  a  kind')
    rank -= 3
  elif dict_repet[2] == 2:
    # print('two pair')
    rank -= 4
  elif dict_repet[2] == 1:
    # print('one pair')
    rank -= 5
  elif dict_repet[1] == 5:
    # print('high card')
    rank -= 6  

  dict_rankings[rank].append(h)

  # print(dict_repet)
  
for k,v in dict_rankings.items():
  print(f'Combo: {k} | Nr of: {len(v)}')


deck = ['A','K', 'Q', 'J', 'T', '9','8', '7', '6', '5', '4', '3', '2']
dict_deck = dict(zip(deck,list(range(0,len(deck)))))
print(dict_deck)

def translate(list_hands):
  tra_hands_dict = {}
  for hand in list_hands:
    tra_hand = ""
    for letter in hand:
      tra_hand += str(dict_deck[letter])
    
    tra_hands_dict[hand] = int(tra_hand)
  tra_hands_dict_ord = dict(sorted(tra_hands_dict.items(), key=lambda x:x[1]))
  return list(tra_hands_dict_ord.keys())

new_rank = 0
current_score = 0 
final_scores = []
for rank, hands in dict_rankings.items():
    new_hands = translate(hands)
    for nhand in new_hands:
      bid = hands_bids[nhand]
      new_rank+=1
      current_score = bid*new_rank
      final_scores.append(current_score)

# print(final_scores)
print(sum(final_scores))
