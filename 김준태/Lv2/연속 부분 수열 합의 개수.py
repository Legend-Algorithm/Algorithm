from collections import defaultdict

def solution(elements):
    dict = defaultdict(int)

    new_elements = elements * 2
    for i in range(1, len(elements) + 1):
        SUM = sum(new_elements[:i])
        m = 0
        dict[SUM] += 1
        for j in range(i, len(new_elements)):
            SUM += new_elements[j] - new_elements[m]
            dict[SUM] += 1
            m += 1
    return len(list(dict.keys()))