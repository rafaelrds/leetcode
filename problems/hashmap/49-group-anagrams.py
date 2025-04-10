from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_key(word):
            freq = [0 for _ in range(26)]
            for c in word:
                freq[ord(c) - ord('a')] += 1
            return "-".join(map(str, freq))

        res = defaultdict(list)
        for word in strs:
            key = get_key(word)
            res[key].append(word)
        return list(res.values())
