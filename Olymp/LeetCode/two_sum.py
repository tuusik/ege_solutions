def twoSum(nums, target):
    l, r = 0, len(nums) - 1
    nums_sorted = sorted(nums)
    while nums_sorted[l] + nums_sorted[r] != target:
        if nums_sorted[l] + nums_sorted[r] < target:
            l += 1
        else:
            r -= 1
    return [nums.index(nums_sorted[l]), len(nums) - nums[::-1].index(nums_sorted[r]) - 1]