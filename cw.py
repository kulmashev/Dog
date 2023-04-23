def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    return False


def plural(n):
    return n != 1