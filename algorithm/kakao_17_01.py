#Bitwise Operation

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

s = []
answer=[]
for i in range(len(arr1)):
  for j in range(1):
    s.append(bin(arr1.pop(0) | arr2.pop(0))[2:])

for k in s:
  cnt=""
  for z in k:
    if z == "1":
      cnt += "#"
    else:
      cnt +=" "
  answer.append(cnt)
print(answer)

# 출력
# ['#####','# # #', '### #','#  ##','#####']