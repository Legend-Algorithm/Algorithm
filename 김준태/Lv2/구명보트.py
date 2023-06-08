from collections import deque

def solution(people, limit):
    answer = 0
    q = deque(sorted(people, reverse=True))

    while q:
        answer += 1
        left = q.popleft()
        if q and left + q[-1] <= limit:
            q.pop()

    return answer