#1
def solution(s):
    stack = 0
    for i in range(len(s)):
        if s[i] == "(":
            stack += 1
        else:
            if stack == 0:
                return False
            else:
                stack -= 1
            
    if stack > 0:
        return False
    else:
        return True
    
#2
def solution(s):
    stack = 0
    for char in s:
        if char == "(":
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
        
    if stack == 0:
        return True
    else:
        return False