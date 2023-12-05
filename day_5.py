import sys

# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  # print(f'Message from stdin: {line}')
  # break
print(txt)

seeds = txt[0].split(": ")[1]
seeds = list(seeds.split(" "))
seeds = [int(s) for s in seeds]

map_name_dict = {}
map_nr = []
map_name = ""
counter = 0
for s in txt[1:]:
  print(s)
  if "map:" in s:
    map_name_dict[s] = map_nr
    map_nr = []

  if s!="" and ":" not in s:
    nrs = s.split(" ")
    nrs = [int(nr) for nr in nrs]
    map_nr.append(nrs)

print(seeds)
print(map_name_dict)

destinations = []
sources = []
map_name_dict_final = {}
dict_v = {}
for map_name,nrs in map_name_dict.items():
    print(map_name)
    map_name_dict_final[map_name] = []
    for l in nrs:
      print(l)
      ini = l[0]
      fin = l[1]
      leng = l[2]
      sour = list(range(fin,fin+leng))
      dest = list(range(ini,ini+leng))

      for i,d in enumerate(dest):
        dict_v[sour[i]] = d

    map_name_dict_final[map_name].append(dict_v)
    dict_v = {}
    
for s in seeds:
  print(f'Seed: {s}')
  current_val = int(s)
  for k,val in map_name_dict_final.items():
    print(k)
    print(val)
    dict_use = val[0]
    if current_val  in dict_use.keys():
      current_val = dict_use[current_val]
    print(current_val)
        
