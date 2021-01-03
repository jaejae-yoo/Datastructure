"""
문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
"""

#풀이 1 (numpy 이용)
import numpy as np
def solution(arr1, arr2):
    answer = []
    for num in range(len(arr1)):
        ans=[]
        cnt = np.array(arr1[num])+np.array(arr2[num])
        for n in cnt:
            ans.append(int(n))
        answer.append(ans)
    return answer

#풀이 2
import numpy as np
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        ans =[]
        for j in range(len(arr1[0])):
            cnt=arr1[i][j] + arr2[i][j]
            ans.append(cnt)
        answer.append(ans)
    return answer