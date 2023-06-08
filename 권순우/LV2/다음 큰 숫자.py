#1
def countones(sen):
    cnt = 0
    for item in sen:
        if item == "1":
            cnt += 1
    return cnt

def solution(n):
    nowsen = str(bin(n))[2:]
    cnt_1 = countones(nowsen)
    while True:
        n += 1
        if countones(str(bin(n))[2:]) == cnt_1:
            break
    return n

#2
def counting1(num):
    res = 0
    binary_num = bin(num)[2:]
    for char in binary_num:
        if char == "1":
            res += 1
    return res
    
def solution(n):
    number_of_1 = counting1(n)
    while True:
        n += 1
        if counting1(n) == number_of_1:
            break            
    return n