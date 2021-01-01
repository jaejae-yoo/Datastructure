"""
문제 설명
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

제한 사항
arr은 길이 1이상, 15이하인 배열입니다.
arr의 원소는 100 이하인 자연수입니다.
"""

def solution(arr):
    _arr = list(reversed(arr[:-1])) #속도 향상을 위해 큰 숫자부터 확인
    cnt,_cnt = arr[-1],1
    while True:
        ans = True
        for num in _arr:
            if cnt%num != 0:
                ans = False
                break
        if ans ==True:
            return cnt
        cnt = _cnt*arr[-1]
        _cnt+=1