#자신보다 큰 수들의 개수를 수열로 표현(역수열_그리디)

n = int(input())
a = list(map(int, input().split()))

list1 = [0] * n

num=1
for i in a:
  cnt =0
  for j in range(i+1):
    if list1[j] < num and list1[j] !=0:
      cnt+=1
  for k in range(cnt+i, n):
    if list1[k] < num and list1[k] != 0:
      cnt+=1
    elif list1[k] == 0:
      break
  list1[cnt+i] = num
  num+=1

print(list1)