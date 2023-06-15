from collections import Counter

def solution(k, tangerine):
    cnt = Counter(tangerine)
    answer = 0
    for i, j in cnt.most_common():
        answer += 1
        k -= j
        if k <= 0:
            break
    return answer