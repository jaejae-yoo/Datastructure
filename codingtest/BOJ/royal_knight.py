#ch04-3

input_data = input()
col = int(ord(input_data[0])) - int(ord('a')) + 1
row = int(input_data[1])

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

count = 0
for step in steps:
  next_row = row + step[0]
  next_column = col + step[1]

  if next_row >= 1 and next_row <=8 and next_column >=1 and next_column<=8:
    count+=1

print(count)