class Sparsematrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.s = [[self.m, self.n, 0]]

    def append(self, i, j, value):
        if value != 0:
            self.s.append([i, j, value])
        self.s[0][2] = len(self.s) - 1

    def shape(self):
        return (self.m, self.n)

    def getValue(self, i, j):
        for k in range(1,len(self.s)):
            if self.s[k][0] == i and self.s[k][1] == j:
                return self.s[k][2]
        return 0

    def print(self):
        import numpy as np
        tmp = np.zeros((self.m, self.n))
        for i in range(1, len(self.s)):
            tmp[self.s[i][0]-1, self.s[i][1]-1] = self.s[i][2]        #0부터 시작
        print(tmp)


    @classmethod
    def add(cls, a, b):
        if a.m != b.m or a.n != b.n:
            return -1
        s = Sparsematrix(a.m, a.n)
        u = set()

        for i in range(1, len(a.s)):
            u.add((a.s[i][0], a.s[i][1]))
        for i in range(1, len(b.s)):
            u.add((b.s[i][0], b.s[i][1]))

        for num in list(u):
            _tmp = a.getValue(num[0], num[1]) + b.getValue(num[0], num[1])
            if _tmp !=0:
                s.append(num[0], num[1], _tmp)
        return s

    @classmethod
    def mult(cls, m1, m2):
        if m1.n == m2.m:
            s0 = Sparsematrix(m1.m, m2.n)
            for i in range(1, m1.m+1):
                for j in range(1, m2.n+1):
                    tmp = 0
                    for k in range(1, m2.n+1):
                        tmp0=m1.getValue(i, k) * m2.getValue(k,j)
                        tmp+=tmp0
                        if tmp !=0:
                            s0.append(i, j, tmp)
            return s0

    def transpose(self, a):
        t_a = Sparsematrix(a.n, a.m)
        for i in range(len(a.s)):
            if i == 0:
                t_a.s[0][2] = a.s[0][2]
            else:
                t_a.append(a.s[i][1], a.s[i][0], a.s[i][2])
        return t_a


v1 = Sparsematrix(3, 3)
v2 = Sparsematrix(3, 3)

v1.append(1, 1, 1)
v1.append(2, 2, 2)
v1.append(3, 3, 3)
v1.print()
print(v1.shape())

v2.append(1, 1, 4)
v2.append(1, 2, 7)
v2.append(2, 3, 2)
v2.append(3, 3, 1)
v2.print()

c = Sparsematrix.add(v1, v2)
c = Sparsematrix.mult(v1, v2)
c.print()