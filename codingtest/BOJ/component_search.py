#ch07-5

N = int(input())
market = list(map(int, input().split()))

M = int(input())
customer= list(map(int, input().split()))
answer =[]
peak = 0

for c in customer:
  correct = "no"
  peak = int(c)
  for m in range(N):
    if peak == market[m]:
      correct = "yes"
    else:
      pass
  answer.append(correct)

for a in answer:
  print(a, end= " ")