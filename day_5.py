import sys

# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  
  # print(f'Message from stdin: {line}')
  # break
# print(txt)

seeds = txt[0].split(": ")[1]
seeds = list(seeds.split(" "))
seeds = [int(s) for s in seeds]

map_name_dict = {}
map_code = []

txt = txt[2:]
txt.append("")

for t in txt:
  # print(t)
  if ":" in t:
    map_name = t
  elif t=="":
    map_name_dict[map_name] = map_code
    map_code = []
  else:
    list_t = [int(t) for t in t.split(" ")]
    map_code.append(list_t)

print(map_name_dict)


final_locations = {}
for s in seeds:
  seed = int(s)
  print(f'\nSeed: {seed}')
  current_val = seed
  found = False

  for k,val in map_name_dict.items():
    for v in val:
      if current_val < v[1] or current_val > v[1] + v[2]:
        next
      else:
        found = True
        current_val = current_val + v[0] - v[1]
        break

  final_locations[s] = current_val

print(final_locations)
print(min(final_locations.values()))
