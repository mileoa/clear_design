def max(a, b):
    # {P: a = n1, b = n2} max(a, b) {Q: (res = a v res = b) ^ res >= a ^ res >= b}
    return a if a >= b else b


def abs(x):
    # {P: x = n} abs(x) {Q: res >= 0 ^ (res = -x v res = x)}
    return x if x >= 0 else -x


def max_of_abs(a, b):
    # {P: a = n1, b = n2} max(abs(a), abs(b)) {Q: ((res >= 0 ^ (res = -a v res = a)) v (res >= 0 ^ (res = -b v res = b))) ^ (res >= 0 ^ res >= a ^ res >= -a) ^ (res >= 0 ^ res >= b ^ res >= -b)}
    # {P: a = n1, b = n2} max(abs(a), abs(b)) {Q: res >= 0 ^ (res = -a v res = a v res = -b v res = b) ^ res >= a ^ res >= -a ^ res >= b res >= -b}
    return max(abs(a), abs(b))
