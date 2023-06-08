#1
def solution(s):
    sen = ""
    blank = True
    for i in range(len(s)):
        ordsi = ord(s[i])
        if ordsi==32:
            sen += chr(ordsi)
            blank = True
        elif 65<=ordsi and ordsi<=90:
            if not blank:
                sen += chr(ordsi+32)
            else:
                sen += chr(ordsi)
            blank = False
        elif 97<=ordsi and ordsi<=122:
            if blank:
                sen += chr(ordsi-32)
            else:
                sen += chr(ordsi)
            blank = False
        else:
            sen += chr(ordsi)
            blank = False
    return sen

#2
def solution(s):
    flag = True
    res = ""
    for char in s:
        if char == " ":
            flag = True
        else:
            if flag:
                char = char.upper()
                flag = False
            else:
                char = char.lower()
        res += char
            
    return res