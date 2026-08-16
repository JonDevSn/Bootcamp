class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time Complexity: O(len(s2))
        Space Complexity: O(1) - 26-character frequency array
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if s1_count[i] == s2_count[i])

        for i in range(n2 - n1):
            if matches == 26:
                return True

            r = ord(s2[i + n1]) - ord('a')
            s2_count[r] += 1
            if s2_count[r] == s1_count[r]:
                matches += 1
            elif s2_count[r] == s1_count[r] + 1:
                matches -= 1

            l = ord(s2[i]) - ord('a')
            s2_count[l] -= 1
            if s2_count[l] == s1_count[l]:
                matches += 1
            elif s2_count[l] == s1_count[l] - 1:
                matches -= 1

        return matches == 26