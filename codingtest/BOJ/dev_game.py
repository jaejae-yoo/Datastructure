# ch04-4
row, col = map(int, input().split())
x, y, direction = map(int, input().split())

# 북, 동, 남, 서, 반시계 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 사용자가 지나간 곳 기록
storage = [[0] * row for _ in range(col)]

road = []
for i in range(row):
    road.append(list(map(int, input().split())))
print(road)


def turn_direction():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


turn_time = 0
count = 1
# 현재 위치 방문 처리
storage[x][y] = 1

while True:
    turn_direction()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if road[nx][ny] == 0 and storage[nx][ny] == 0:
        turn_time = 0
        x = nx
        y = ny
        count += 1
        storage[nx][ny] = 1
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if road[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)