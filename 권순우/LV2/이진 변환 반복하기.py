#1
def solution(s):
    trans = 0
    cutzero = 0
    while s != "1":
        sen = ""
        for char in s:
            if char == "0":
                cutzero += 1
            else:
                sen += char
        s = str(bin(len(sen)))[2:]
        trans += 1
    return [trans,cutzero]

#2
def solution(s):
    count_0 = 0
    step = 0
    
    while True:
        step += 1
        count_1 = 0
        
        #step1
        for char in s:
            if char == "1":
                count_1 += 1
            else:
                count_0 += 1
        if s=="1":
            break
            
        #step2
        s = bin(count_1)[2:]
        if s =="1":
            break
            
    return [step,count_0]