class Solution:
    # хорошая память
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]: return True
        return False
    
    # среднее время и средняя память
    def containsDuplicate(self, nums) -> bool:
        if len(set(nums)) == len(nums): return False
        else: return True