def Two_sum(numbers, target):
    
    left, right = 0, len(numbers) - 1
    while left < right: # distinct
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left, right]
        if curr_sum < target:
            left += 1
        else :
            right -= 1
    return []

numbers = [2, 7, 13, 15, 17]
print(Two_sum(numbers, target=9))
