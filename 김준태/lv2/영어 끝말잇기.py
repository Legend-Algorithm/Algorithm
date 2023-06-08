from collections import defaultdict

def solution(n, words):
    count = 0
    word = defaultdict(int)
    while count < len(words):
        if word[words[count]] or len(words[count]) < 1 or (count > 0 and words[count][0] != words[count - 1][-1]):
            return [count % n + 1, count // n + 1]

        word[words[count]] += 1
        count += 1

    return [0, 0]