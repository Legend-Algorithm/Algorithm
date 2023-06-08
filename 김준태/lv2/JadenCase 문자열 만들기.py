def solution(s):
    ans = ""
    i = 0
    while i < len(s):
        if s[i] != ' ':
            ans += s[i].upper()
            i += 1
            while i < len(s) and s[i] != ' ':
                ans += s[i].lower()
                i += 1
        else:
            ans += s[i]
            i += 1
    return ans