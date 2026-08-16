class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1) - bounded by the character set size (ASCII <= 256)
        """
        map_s_t = {}
        map_t_s = {}

        for c1, c2 in zip(s, t):
            if (c1 in map_s_t and map_s_t[c1] != c2) or (c2 in map_t_s and map_t_s[c2] != c1):
                return False
            map_s_t[c1] = c2
            map_t_s[c2] = c1

        return True