class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    """
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        if(m == 0 or n == 0): return 0
        if(m == 1 and n == 1): return 1

        if((m,n) in memo): return memo[(m,n)]

        memo[(m,n)] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m, n - 1, memo)

        return memo[(m,n)]
    """

s = Solution()
print(s.uniquePaths(2,3))