import sys
import string

# read input
txt = []
for line in sys.stdin:
    line = line.rstrip()
    txt.append(line)
    
print(txt)


### PART 1
dict_cube_allowed = {'red':12,'green':13,'blue':14}
total_sum_allowed = 0
games_not_allowed = []

### PART 2 
powers = []

for g in txt:
  game_z = g.split(": ")
  game_nr = game_z[0].split("Game ")[1]
  subsets = game_z[1].split("; ")
  games_dict_max = {'red':0,'blue':0,'green':0}

  for s in subsets:
    t = s.split(", ")
    for val in t:
      nr = val.split(" ")[0]
      color = val.split(" ")[1]
      if int(nr) >= games_dict_max[color]:
        games_dict_max[color] = int(nr)
    
  # part 2
  power = 1
  for p in games_dict_max.values():
    power *= p
  powers.append(power)

  # part 1
  for color, nr in dict_cube_allowed.items():
    if nr < games_dict_max[color]:
      games_not_allowed.append(int(game_nr))
      break
  total_sum_allowed += int(game_nr)
  
print(games_not_allowed)
print(f'Part 1: {total_sum_allowed-sum(games_not_allowed)}')
print(f'Part 2: {sum(powers)}')
        
