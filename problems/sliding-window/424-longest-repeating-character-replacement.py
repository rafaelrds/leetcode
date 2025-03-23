class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def char_position(c):
            return ord(c) - ord('A')

        def is_valid(arr):
            tmp = k
            max_val = float('-inf')
            for i, x in enumerate(arr):
                if x > max_val:
                    max_val = x
                    max_index = i

            for i, x in enumerate(arr):
                if i != max_index:
                    tmp -= x
            return tmp >= 0

        count = [0] * 26
        res = float('-inf')
        l = r = 0
        while r < len(s):
            c = s[r]
            count[char_position(c)] += 1
            if is_valid(count):
                res = max(res, r - l + 1)
                r += 1
            else:
                c = s[l]
                count[char_position(c)] -= 1
                l += 1
                r += 1

        return res
