# Time Complexity: O(n)
# Reason: computes each Fibonacci number once in a bottom-up loop
# Space Complexity: O(n) for the DP table
# Drawbacks:
# 1) uses more memory than necessary (full array when only last two values are needed)
# 2) must compute all values up to n sequentially (cannot jump directly to F(n))

def fib_dp(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    print(fib_dp(10))
