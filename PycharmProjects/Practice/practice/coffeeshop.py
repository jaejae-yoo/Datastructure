#queue를 활용하여 coffeshop 대기시간 관리
import numpy as np
import random

class cqueue:                             #대기하고 있는 고객을 관리하는 cqueue 클래스를 생성합니다.
    def __init__(self):
        self.cq=[]

    def push(self, item):
        self.cq.append(item)

    def lastpeek(self):
        if len(self.cq) >0:
            return self.cq[-1]
        else:
            return None

    def size(self):
        return len(self.cq)

    def isempty(self):
        if len(self.cq) >0:
            return False
        else:
            return True

    def peek(self):
        if self.isempty() == False:
            return self.cq[0]

    def pop(self):
        if self.size() > 0:
            return self.cq.pop(0)
        else:
            return None

class cust:
    def __init__(self):
        pass

    def arrivetime(self):                      #고객의 도착시간을 관리합니다.
        x = np.random.exponential(1, 1000)
        self.entTime = np.cumsum(x)             #고객의 도착 시간을 하나씩 누적합니다.
        return self.entTime

    def outTime(self, ordertime):                   #고객의 나가는 시간을 관리합니다.
        cookTime = np.random.normal(1, 0.2, 100)                #평균적으로 cookTime은 1분이 걸리고 ,표준 편차는 0.2로 설정해주어 값 100개를 만듭니다.
        self.cookTime = np.where(cookTime < 0, 1, cookTime)     #음수가 나오는 경우는 cookTime을 평균 값인 1로 해줍니다.
        cook = random.choice(self.cookTime)           #self.cookTime중에서 램덤으로 하나를 추출하여 하나의 값을 return 해줍니다.
        return (ordertime + cook)


class shop:                           #coffee shop 클래스를 생성합니다.
    def __init__(self):
        self.q = cqueue()

    def getsize(self):
        return len(self.q.cq)

    def entcust(self, customer):
        self.q.push(customer)

    def outcust(self):
        self.q.pop()

    def getlast(self):
        return self.q.lastpeek()

    def print(self):
        return print(self.q.cq)

s=shop()
c = cust()
arrive = c.arrivetime()       #손님 도착 시간을 받아옵니다.
curtime =0                    #카페 오픈 시간을 현재 시각 0(8am)으로 초기화 해줍니다.

for arrivetime in arrive:
    curtime = arrivetime
    if curtime >= 0 and curtime <60*14:       #주문시간이 가능한 시간은 아침 8am부터 10pm 까지이다.(14*60 = 840)
        while s.getsize() > 0 and s.q.peek() < curtime:  #queue 안에 있는 시간중에 curtime 보다 작은 값은 모두 삭제합니다.
            s.outcust()
        if s.getsize() ==0:                 #만약 queue의 size가 0이라면 대기인원이 없는 것입니다.
            ordertime = arrivetime                      # 따라서 도착 시간이 ordertime 입니다.
            outtime = c.outTime(ordertime)
        else:
            ordertime = s.getlast()           #ordertime은 마지막으로 들어간 고객의 나가는 시각입니다.
            outtime = c.outTime(ordertime)         #위에서 구한 ordertime에 cooktime을 더한 것인 outtime 입니다.
        s.entcust(outtime)
    else:
        if s.getsize() != 0:                            #10pm이전에 주문하여 대기 queue에 있는 고객들에게만 음료를 제공하고 break합니다.
            for i in range(s.getsize()):
                s.outcust()
            break

    s.print()
    print(arrivetime, ordertime, outtime, s.getsize())

s.print()            #장사를 모두 마친 뒤에는 coffee shop의 대기인원은 없는 것을 확인할 수 있습니다.






