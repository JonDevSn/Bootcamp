# check valid anagram using hashing
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    m = {}
    for i in s:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    for j in t:
        if j in m:
            m[j] -= 1
        else:
            return False
    for k in m.values():
        if k != 0:
            return False
    return True

               