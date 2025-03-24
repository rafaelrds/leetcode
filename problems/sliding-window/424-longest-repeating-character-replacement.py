class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def char_position(c):
            return ord(c) - ord('A')

        def is_valid(arr, l, r):
            max_f = max(arr)
            return r - l + 1 - max_f <= k

        count = [0] * 26
        res = float('-inf')
        l = r = 0
        while r < len(s):
            c = s[r]
            count[char_position(c)] += 1
            if is_valid(count, l ,r):
                res = max(res, r - l + 1)
                r += 1
            else:
                c = s[l]
                count[char_position(c)] -= 1
                l += 1
                r += 1

        return res
