#binarytree에서 노드 사이의 거리 계산

class binarytree:
    def __init__(self):
        self.bt=[None]

    def print(self):
        print(self.bt)

    def append(self, item):
        self.bt.append(item)

    def size(self):
        return len(self.bt)-1

    def getchild(self,item):
        if item in self.bt:
            k = self.bt.index(item)
            num = k
            if num*2 <= self.size():
                print(self.bt[num*2])
            else:
                print(None)
            if num * 2 + 1 <= self.size():
                print(self.bt[num * 2 + 1])
            else:
                print(None)
        else:
            print("item not found")

    def getparent(self, item):
        if item in self.bt:
            num = self.bt.index(item)
            k = num//2
            if k > 0:
                print(self.bt[k])
            else:
                print(None)
        else:
            print("item not found")

    def height(self):
        _tmp = 0
        n = self.bt[-1]
        num = self.bt.index(n)
        if num == 1:
            return 0
        else:
            while True:
                num=num//2
                _tmp+=1
                if num == 1:
                    return _tmp


    def getdistance(self, item1, item2):
        cnt=0
        if item1 in self.bt:
            k1=self.bt.index(item1)
        else:
            print(item1+" not found")
        if item2 in self.bt:
            k2 = self.bt.index(item2)
        else:
            print(item2+" not found")

        for i in range(self.height()+1):
            if k1 == k2:
                print(str(cnt)+"/"+str(self.height()))
                break
            else:
                k1=k1//2
                k2=k2//2
            cnt += 1

bt = binarytree()
bt.append("호흡기/소화기병")
bt.append("호흡기병")
bt.append("소화기병")
bt.append("호흡기감염")
bt.append("폐질환")
bt.append("위질환")
bt.append("결장질환")
bt.append("독감")
bt.append("기관지염")
bt.append("폐부종")
bt.append("폐색전증")
bt.append("위궤양")
bt.append("위암")
bt.append("대장염")
bt.append("대장암")

bt.getdistance("대장염", "대장암") #대장염과 대장암의 관련도
bt.getdistance("대장염", "위궤양")
bt.getdistance("독감", "대장암")




