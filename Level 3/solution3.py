import test

def solution(n):
    # Your code here
    steps = 0
    num = int(n)
    while num > 1:
        if num & 1 == 0:
            num /= 2
        elif num == 3 or num & 3 == 1:
            num -= 1
        else:
            num += 1
        steps += 1

    return steps

test.testEqual(solution('15'), 5)
test.testEqual(solution('4'), 2)

