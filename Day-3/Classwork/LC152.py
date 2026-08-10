class Solution(object):
    def maxProduct(self, nums):
        curr_max = nums[0]
        curr_min = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Negative number swaps max and min
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            answer = max(answer, curr_max)

        return answer