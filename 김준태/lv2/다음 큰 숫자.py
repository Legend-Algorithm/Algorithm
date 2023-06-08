def conv_2(n):
    count_1 = 0
    for i in str(bin(n)):
        if i == '1':
            count_1 += 1
    return count_1


def solution(n):
    count_1 = conv_2(n)

    while True:
        n += 1
        if conv_2(n) == count_1:
            break

    return n