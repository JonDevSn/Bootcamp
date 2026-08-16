# check duplicate elements using hashing
def check_duplicate(arr):
    m = {}
    for i in arr:
        if i in m:
            return True
        else:
            m[i] = 1
    return False 