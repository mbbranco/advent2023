import sys
import numpy as np
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  # print(f'Message from stdin: {line}')
  # break
print(txt)

parts = txt[txt.index("")+1:]
instructions = txt[0:txt.index("")]

dict_instructions = {}
instructions = [i[0:-1].split("{") for i in instructions]
for i in instructions:
  dict_instructions[i[0]] = i[1].split(",")

parts = [i[1:-1].split(",") for i in parts]
parts_final = []
for part in parts:
  dict_parts = {}
  for p in part:
    dict_parts[p[0]] = int(p[2:])
    
  parts_final.append(dict_parts)
    
# print(parts_final)
# print(dict_instructions)
# print()
val_acc = 0
for part in parts_final:
  def check(step):

    condition = step.split(":")[0]
    result = step.split(":")[1]
      
    condition_sign = condition[1]
    condition_val = int(condition[2:])
    condition_char = condition[0]
    char_value = part[condition_char]
    
    char_result = "?"
    if condition_sign == ">":
      if char_value > condition_val:
        char_result = result
    elif condition_sign == "<":
      if char_value < condition_val:
        char_result = result
    else:
      char_result = result

    return char_result
  
  # print()

  # print(part)
  inst = dict_instructions['in']

  # print(f'Instruction: {inst}')
  step_max = len(inst)-1
  finish  = False
  i = 0
  values = 0
  while finish == False:
    # print(f'Step: {inst[i]}')

    step = inst[i]
    # print(step)
    if ":" not in step:
      # print("last")
      next_res = step
    else:
      next_res = check(step)
      
    if next_res == '?':
      # print('next')
      i+=1
    else:
      if next_res == 'A':
        # print('Accepted')
        print(sum(part.values()))
        val_acc+= sum(part.values())
        finish = True
      elif next_res == 'R':
        # print('Rejected')
        finish = True
      else:
        # print('Move')
        inst = dict_instructions[next_res]
        step_max = len(inst)-1
        # print(f'New Instruction: {inst}')
        i=0

print(val_acc)
    
