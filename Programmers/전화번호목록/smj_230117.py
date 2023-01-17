def solution(phone_book):
    f = sorted(phone_book, key = lambda x : (x, len(x)))
    for idx in range(len(f)-1):
        if f[idx+1].startswith(f[idx]):
            return False
    return True
