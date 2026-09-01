class Solution(object):
    def subsets(self, nums):
        ans = []
        current = []

        def backtrack(index):
            # Base case
            if index == len(nums):
                ans.append(current[:])
                return

            # Choice 1: Take nums[index]
            current.append(nums[index])
            backtrack(index + 1)

            # Backtrack
            current.pop()

            # Choice 2: Don't take nums[index]
            backtrack(index + 1)

        backtrack(0)
        return ans