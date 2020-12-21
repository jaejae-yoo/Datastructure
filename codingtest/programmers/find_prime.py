"""
<완전 탐색>
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다."""

from itertools import permutations


def solution(numbers):
    _list = []
    for i in range(len(numbers)):
        _list.append(list(map(''.join, permutations(numbers, i + 1))))

    b = set()
    for j in _list:
        for k in range(len(j)):
            if int(j[k]) == 1:
                pass
            else:
                b.add(int(j[k]))
    ans = []
    for num in b:
        is_prime = True
        for n in range(2, int(num)):
            if num % n == 0:
                is_prime = False
                break
        if is_prime == True and int(num) != 0:
            ans.append(num)
    return len(ans)