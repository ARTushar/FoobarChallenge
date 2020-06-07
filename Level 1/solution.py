def solution(area):
    import math
    ans = []
    remaining_area = area
    start = area
    while start > 0:
        # print(start)
        if math.sqrt(start).is_integer():
            ans.append(start)
            start = remaining_area - start
            remaining_area = start
        else:
            start -= 1
    return ans

print(solution(5))
print(solution(15324))