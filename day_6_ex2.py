import sys
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  
print(txt)

txt = [t.split(': ') for t in txt]
lists = []
for t in txt:
  a = t[1].split(" ")
  a = [int(x) for x in a if x!=""]
  lists.append(a)

times = lists[0]
distances = lists[1]
  
print(lists)

race_record = {}
new_record = 0
for race_nr in range(0,len(times)):
  race_time = times[race_nr]
  race_dist = distances[race_nr]
  # print(race_time)
  # print(race_dist)
  def calc_distance(val):
    hold_time = val
    speed = hold_time*1
    remain_time = race_time - hold_time
    distance = remain_time * speed

    if distance > race_dist:
      print('Record!')
    return distance
      
  print(f'\nRace: {race_nr}')
  min_value = race_dist//race_time
  if race_dist/race_time-min_value >= 0.5:
    min_value+=1
    
  print(f'Min Value: {min_value} | Dist {calc_distance(min_value)}')

      
  max_value = race_time//2
  
  print(f'Max Value: {max_value} | Dist {calc_distance(max_value)}')
  nr_records = range(min_value,max_value)
  print(len(nr_records)*2)
