#백준 1654

def count(lines, n):
    cnt = 0
    for line in lines:
        cnt += line // n
    return cnt

f = open("파일 경로", 'r')
k, n = map(int, f.readline().split())
lines = []
for i in range(k):
    lines.append(int(f.readline()))

mini = 1
maxi = max(lines)
mid = (mini + maxi) // 2

while True:
    if count(lines, mid) > n:
        mini = mid
    elif count(lines, mid) < n:
        maxi = mid
    else:
        mini = mid + 1
        if mini == maxi:
            break
    mid = (mini + maxi) // 2
print(mid)