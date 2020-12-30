def solution(numbers, target):
    n = len(numbers)
    cnt =0
    def dfs(L, total):
        if L == n:
            if total == target:
                nonlocal cnt
                cnt+=1
            else:
                dfs(L+1, total + numbers[L])
                dfs(L+1, total - numbers[L])

    dfs(0,0)
    return cnt

solution([1,1,1,1,1],3)