import test


def solution(start, length):

    def xor_upto_n(n):
        ans = [n, 1, n+1, 0]
        return ans[n % 4]

    def xor_a_to_b(a, b):
        return xor_upto_n(a-1) ^ xor_upto_n(b)

    checksum = 0
    a = start
    b = start + length - 1
    for i in xrange(length):
        checksum ^= xor_a_to_b(a, b)
        a = a + length
        b = b + length - 1

    return checksum


test.testEqual(solution(0, 1), 0)
test.testEqual(solution(17, 4), 14)
