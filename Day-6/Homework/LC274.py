class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(citations)
        buckets = [0] * (n + 1)

        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1

        total = 0
        for i in range(n, -1, -1):
            total += buckets[i]
            if total >= i:
                return i

        return 0