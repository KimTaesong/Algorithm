def solution(n):
    nums = ['4', '1', '2']
    num = ''
    while n > 0:
        mod_value = n % 3
        n = n // 3
        if mod_value == 0:
            n -= 1
        num = nums[mod_value] + num
    return num


print(solution(6))
