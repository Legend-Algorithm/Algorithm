from math import gcd

def solution(arr):
    num = arr[0]
    for i in range(1, len(arr)):
        num = num * arr[i] // gcd(num, arr[i])
    return num