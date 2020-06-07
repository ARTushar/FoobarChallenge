def solution(l, t):
    # Your code here
    begin = 0

    while begin < len(l):
        end = begin
        sum = 0
        while end < len(l):
            sum += l[end]
            if sum == t:
                return [begin, end]
            end += 1
        begin += 1

    return [-1, -1]

print(solution([1, 2, 3, 4], 12))
print(solution([1, 2, 3, 4], 15))
print(solution([4, 3, 10, 2, 8], 12))
print(solution([4, 3, 5, 7, 8], 12))
print(solution([1, 2], 2))



