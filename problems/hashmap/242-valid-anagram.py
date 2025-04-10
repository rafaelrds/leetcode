class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            Given two strings s and t, return true if t is an anagram of s, and false otherwise
        """
        if len(s) != len(t):
            return False

        freq = [0 for _ in range(26)]
        for c1, c2 in zip(s, t):
            freq[ord(c1) - ord('a')] += 1
            freq[ord(c2) - ord('a')] -= 1

        return all(map(lambda x: x == 0, freq))
