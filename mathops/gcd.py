def computeGCD(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


if __name__ == "__main__":
    # we can write tests here
    assert computeGCD(12, 18) == 6
