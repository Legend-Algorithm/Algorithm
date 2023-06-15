def solution(n):
    prev = 1
    nxt = 1
    while n > 0:
        n -= 1
        prev, nxt = nxt, prev + nxt
    return prev % 1234567