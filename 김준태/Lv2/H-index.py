def solution(citations):
    answer = 0
    while True:
        answer += 1
        cnt = 0
        for i in citations:
            if i >= answer:
                cnt += 1
        if cnt < answer:
            answer -= 1
            break
    return answer