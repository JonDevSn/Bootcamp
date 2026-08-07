class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        nums = list(set(nums))
        if len(nums) >= 3 :
            maxm = max(nums)
            nums.remove(maxm)
            maxm = max(nums)
            nums.remove(maxm)
            maxm = max(nums)
            return maxm
        else : 
            return max(nums)
