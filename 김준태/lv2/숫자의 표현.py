from collections import deque

def solution(n):
    answer = 0
    q = deque(range(1, n + 1))
    s = deque()
    Sum = 0
    while q:
        num = q.popleft()
        Sum += num
        s.append(num)
        if Sum == n:
            answer += 1
        if Sum > n:
            while s and Sum > n:
                Sum -= s.popleft()
            if Sum == n:
                answer += 1
    return answer