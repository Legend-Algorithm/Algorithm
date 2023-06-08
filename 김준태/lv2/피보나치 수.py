def solution(n):
    answer = 0
    num1, num2 = 1, 1
    for _ in range(n - 2):
        num1, num2 = num2, num1 + num2
    return num2 % 1234567