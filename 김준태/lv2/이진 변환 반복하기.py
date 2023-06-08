def solution(s):
    cnt = 0
    ans = 0
    while s != '1':
        count_0 = 0
        count_1 = 0
        for i in s:
            if i == "0":
                count_0 += 1
            else:
                count_1 += 1
        s = bin(count_1)[2:]
        cnt += 1
        ans += count_0
    return [cnt, ans]