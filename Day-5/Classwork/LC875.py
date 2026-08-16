class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Time Complexity: O(n * log(max(piles))) where n is len(piles)
        Space Complexity: O(1)
        """
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours <= h:
                right = mid
            else:
                left = mid + 1

        return left