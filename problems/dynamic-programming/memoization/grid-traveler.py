class Solution:
    """
        Calculates in how many ways can we from (0, 0) to (m, n) in a 2D grid.
    """
    def grid_traveler(self, n: int, m: int, memo=None) -> int:
        if memo is None:
            memo = {}
        pair = (min(m, n), max(m, n))
        if pair in memo:
            return memo[pair]
        if n == 1 and m == 1:
            return 1
        if n == 0 or m == 0:
            return 0

        memo[pair] = self.grid_traveler(n - 1, m, memo) + self.grid_traveler(n, m - 1, memo)
        return memo[pair]


if __name__ == "__main__":
    s = Solution()
    assert s.grid_traveler(1, 1) == 1
    assert s.grid_traveler(2, 3) == 3
    assert s.grid_traveler(3, 2) == 3
    assert s.grid_traveler(3, 3) == 6
    assert s.grid_traveler(18, 18) == 2333606220

    print("OK")
