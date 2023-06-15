from collections import deque

def solution(s):
    answer = 0
    q = deque(s)
    for _ in range(len(q)):
        stack = []
        for i in q:
            if not stack:
                stack.append(i)
            elif stack and stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack and stack[-1] == '{' and i == '}':
                stack.pop()
            elif stack and stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            answer += 1
        q.rotate(-1)
    return answer