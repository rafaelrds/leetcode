class Solution:
    def fibonacci(self, n: int, memo=None) -> int:
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n <= 0:
            raise ValueError("The Fibonacci sequence starts at n = 1")
        if n <= 2:
            return 1
        memo[n] = self.fibonacci(n - 1, memo) + self.fibonacci(n - 2, memo)
        return memo[n]


if __name__ == "__main__":
    # Sequence is [1, 1, 2, 3, 5, 8, 13, 21...]
    s = Solution()
    for i in range(1, 50):
        print(s.fibonacci(i))