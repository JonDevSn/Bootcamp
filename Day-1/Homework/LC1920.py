class Solution(object):
    def buildArray(self, nums):
        result = []
        a = 0
        for i in range(0,len(nums)):
            a = nums[nums[i]]
            result.append(a)
        return result
        