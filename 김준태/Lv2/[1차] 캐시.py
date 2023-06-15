def solution(cacheSize, cities):
    answer = 0
    q = []
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        check = 0
        for i in range(len(q)):
            if q[i] == city:
                q.pop(i)
                q = [city] + q
                check = 1
                answer += 1
                break
        if check:
            continue
        if len(q) < cacheSize:
            q = [city] + q
            answer += 5
        else:
            q.pop()
            q = [city] + q
            answer += 5
    return answer

