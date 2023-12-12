import sys
# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  
instructions = [t for t in txt[0]]
# print(instructions)

dict_nodes = {}
starting_nodes = []
for t in txt[2:]:
  node, p = t.split(" = ")
  l,r = p.split(", ")
  dict_nodes[node] = [l[1:],r[:-1]]
  if node[-1] == 'A':
    starting_nodes.append(node)
    
# print(dict_nodes)
# print(starting_nodes)

new_nodes = []
for start in starting_nodes:
  node = start
  i=0
  n_steps = 0
  found = False
  while found == False:
    # print(node)
    instr = instructions[i]
  
    if instr =='R':
      node = dict_nodes[node][1]
    else:
      node = dict_nodes[node][0]
      
    n_steps+=1
  
    if node[-1]=='Z':
      found = True
      new_nodes.append(n_steps)
      n_steps = 0

    if i+1 == len(instructions):
      i=0
    else:
      i+=1


print(new_nodes)

# defining a function to calculate LCM  
# Function to calculate the GCD of two numbers
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to calculate the LCM of two numbers
def lcm(x, y):
    return x * y // gcd(x, y)

# Function to calculate the LCM of a list of numbers
def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result
    
result = lcm_of_list(new_nodes)
print(result)
