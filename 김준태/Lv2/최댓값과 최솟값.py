# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    num = list(map(int, s.split()))
    return f'{min(num)} {max(num)}'