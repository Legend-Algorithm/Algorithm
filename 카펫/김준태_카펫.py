def solution(brown, yellow):
    total = brown + yellow

    for i in range(3, total):
        if total % i == 0:
            w, h = total // i, i
            if yellow == (w - 2) * (h - 2):
                return [w, h]