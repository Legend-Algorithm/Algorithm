#1
def solution(s):
    nums = list(map(int,s.split()))
    maxnum = nums[0]
    minnum = nums[0]
    for i in range(len(nums)):
        newnum = nums[i]
        maxnum = max(maxnum,newnum)
        minnum = min(minnum,newnum)
    return str(minnum)+" "+str(maxnum)

#2
def solution(s):
    numarr = list(map(int,s.split(" ")))
    return str(min(numarr)) + " " + str(max(numarr))