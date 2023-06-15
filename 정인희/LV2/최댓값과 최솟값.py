def solution(s):
    answer = ''
    s=list(map(int,s.split()))
    s.sort()
    _min=str(min(s))
    _max=str(max(s))
    answer+=_min
    answer+=" "
    answer+=_max
    print(answer)
    return answer