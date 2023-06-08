#1
def solution(A,B):
    res = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        res = res + A[i]*B[i]
    return res

#2
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    res = 0
    for i in range(len(A)):
        res += A[i] * B[i]
        
    return res