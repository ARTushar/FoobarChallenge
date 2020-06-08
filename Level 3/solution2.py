import test

def solution(l):
    # Your code here
    count = 0
    i = 0
    d = {}
    while i < len(l):
        first = l[i]
        j = i + 1
        while j < len(l):
            second = l[j]
            if second % first == 0:
                mid_count = d.get((j, second), -1)
                if mid_count == -1:
                    mid_count = 0
                    k = j + 1
                    while k < len(l):
                        third = l[k]
                        if third % second == 0:
                            mid_count += 1
                        k += 1
                    d[(j, second)] = mid_count
                count += mid_count
            j += 1
        i += 1
    
    return count

test.testEqual(solution([1, 1, 1]), 1)
test.testEqual(solution([1, 2, 3, 4, 5, 6]), 3)
test.testEqual(solution([1, 2, 4, 8, 16, 5, 10, 15]), 13)

