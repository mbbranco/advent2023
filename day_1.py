import sys

# read input
txt = []
for line in sys.stdin:
  line = line.rstrip()
  txt.append(line)
  # print(f'Message from stdin: {line}')
  # break
  
print(txt)

# input list
num_int = ['1','2','3','4','5','6','7','8','9']

#### for part 1:
num_ext = []

#### for part 2:
num_ext = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dict_num_ext = dict(zip(num_ext,num_int))

all_nums = num_ext.copy()
all_nums.extend(num_int)


digs = []
for word in txt:
val = {}
for n in all_nums:
  # for each word in list, check if any number is on the string
  if n in word:
    
    # convert full number to digit
    if n in num_ext:
      val_int = dict_num_ext[n]
    if n in num_int:
      val_int = n
    
    # check if value is more than once in the word
    counter = word.count(n)
    if counter == 1:
      # if not, then save the first position
      val[word.find(n)] = val_int
    else:
      # if yes then save the most left position and the most right position
      lfind = word.find(n)
      rfind = word.rfind(n)
      val[lfind] = val_int
      val[rfind] = val_int
    
# order the dictionary by position
ord_pos = dict(sorted(val.items()))
vals = list(ord_pos.values())
# get the first and last digit
soma = vals[0]+vals[-1]
# append the two digits and convert to the integer form 
digs.append(int(soma))

# get the final sum
print(sum(digs))
