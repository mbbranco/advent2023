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
  
  for hold_time in range(0,race_time):
    speed = hold_time*1
    remain_time = race_time - hold_time
    distance = remain_time * speed
    print(distance)
    # print()
    if distance > race_dist:
      new_record+=1
  
  race_record[race_nr] = new_record
  new_record = 0
print(race_record)

nr_records = race_record.values()
total = 1
for n in nr_records:
  total *= n
print(total)
