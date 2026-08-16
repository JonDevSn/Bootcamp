class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        invert_count = 0

        while n > 1:
            mid = 1 << (n - 1)
            if k == mid:
                return "1" if invert_count % 2 == 0 else "0"
            elif k > mid:
                k = 2 * mid - k
                invert_count += 1
            n -= 1

        return "0" if invert_count % 2 == 0 else "1"