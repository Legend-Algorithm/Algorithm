def solution(n, left, right):
    answer = []
    start = left // n + 1
    finish = (right + 1) // n + ((right + 1) % n != 0)
    slice_left = left - (start - 1) * n
    slice_right = right + 1 - finish * n
    for i in range(start, finish + 1):
        answer += [i] * i
        for j in range(i + 1, n + 1):
            answer.append(j)
    if slice_right == 0:
        return answer[slice_left:]
    else:
        return answer[slice_left:slice_right]