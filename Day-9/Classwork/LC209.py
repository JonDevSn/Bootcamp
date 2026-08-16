class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        w_sum = 0
        ans = float('inf')
        for right in range(len(nums)):
            w_sum += nums[right]

            while w_sum >= target :
                ans = min(ans,right - left + 1)
                w_sum -= nums[left]
                left += 1 
        
        if ans == float('inf') :
            return 0
        else:
            return ans
