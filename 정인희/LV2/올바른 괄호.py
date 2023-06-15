def solution(s):
    answer = True
    s=list(s)
    if len(s)%2!=0 or s[0]!='(':
        return False
    stack=[]
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False
