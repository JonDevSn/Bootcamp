class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        Time Complexity: O(n * log(sum(weights) - max(weights)))
        Space Complexity: O(1)
        """
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2

            needed_days = 1
            current_load = 0

            for w in weights:
                if current_load + w > mid:
                    needed_days += 1
                    current_load = 0
                current_load += w

            if needed_days <= days:
                right = mid
            else:
                left = mid + 1

        return left