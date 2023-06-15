from collections import Counter


def solution(k, tangerine):
    answer = 0

    counters = dict(Counter(tangerine))

    counters = sorted(counters.items(), key=lambda x: x[1], reverse=True)
    # print(counters)

    for counter in counters:
        k -= counter[1]
        answer += 1
        if k <= 0:
            break
    return answer