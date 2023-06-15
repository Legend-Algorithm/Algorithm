def solution(s):
    answer = ''

    l = []
    l.append(s.split(' '))
    # l.append(list(map(list,s.split(' '))))
    # print(l)

    for i in s.split(' '):
        i = str(i)
        i = i.capitalize()
        print(i)
        answer += i
        answer += " "
    answer = answer[:-1]
    print(answer)
    return answer