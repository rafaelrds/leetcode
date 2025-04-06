from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0: # TODO: what happens if this is removed?
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != (amount + 1) else -1


if __name__ == "__main__":
    s = Solution()
    res = s.coinChange([1, 3, 4, 5], 7)
    print(res, res == 2) # 3, 4
    res = s.coinChange([1, 2], 8)
    print(res, res == 4) # 2,2,2,2 = 4 coins
