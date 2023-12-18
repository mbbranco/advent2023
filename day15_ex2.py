import sys
import numpy as np
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  

corr = txt[0].split(",")
# print(corr)

boxes_dict = {}
for c in corr:
  if "-" in c:
    pos = c.index("-")
    op = "-"
  elif "=" in c:
    pos = c.index("=")
    op = "="
    
  label = c[0:pos]

  if op =="-":
    focal_len = 0
  else:
    focal_len = int(c[pos+1:])
    
  label_focal_len = [label,focal_len]
  current_value = 0

  for char in label:
    ascii_val = ord(char)
    current_value += ascii_val
    current_value *= 17
    current_value = current_value % 256
    
  box = current_value
  # print(boxes_dict)
  # print(f'\nBox: {box} | Operation: {label_focal_len}')

  if box in boxes_dict.keys():
    lenses = boxes_dict[box]
    # print(lenses)
    label_found = False
    for i,l in enumerate(lenses):
      # print(l)
      if l[0] == label and op=="-":
        # print("retirar")
        new_lenses = lenses[0:i] + lenses[i+1:]
        # print(new_lenses)
        boxes_dict[box] = new_lenses
        label_found = True
        break

      if l[0] == label and op=="=":
        # print("trocar")
        new_lenses = lenses.copy()
        new_lenses[i] = label_focal_len
        boxes_dict[box] = new_lenses
        label_found = True
        break
    
    if not label_found and op=="=":
      boxes_dict[box].append(label_focal_len)
      
  else:
    boxes_dict[box] = [label_focal_len]

# print(boxes_dict)


#calculate power
powers = []
for box,lenses in boxes_dict.items():
  total_power = 0
  for i,l in enumerate(lenses):
    box_val = box+1
    slot_val = i+1
    focal_len = l[1]
    total_power = box_val * slot_val * focal_len
    powers.append(total_power)

print(powers)
print(sum(powers))
