def solution(arr):
    answer = 0
    _max = max(arr)

    cnt = 1

    while True:
        flag = 0
        temp = _max * cnt

        for i in arr:
            if temp % i != 0:
                flag = 1
                break

        if flag == 0:
            return temp

        cnt += 1

    return answer