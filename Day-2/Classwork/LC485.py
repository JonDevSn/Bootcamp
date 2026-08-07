class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        Max = 0
        count = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count += 1
            else :
                count = 0
            Max = max(Max,count)
        return Max
        