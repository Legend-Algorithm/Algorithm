#1
def solution(n):
    ans = 0
    for i in range(1,n+1):
        if i%2==1:
            if n%i==0 and n//i-i//2 >= 1:
                print(i)
                ans += 1
        else:
             if n%(2*(n//i)+1)==0 and n//(i//2) // 2 - i//2 >= 0:
                print(i)
                ans += 1
            
    return ans

#2
def solution(n):
    arr = [0]
    summed = 0
    for i in range(1,n+1):
        summed += i
        arr.append(summed)
        
    res = 0
    
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j]-arr[i]==n:#정답
                res += 1
                break
            if arr[j]-arr[i]>n:#초과
                break
    return res