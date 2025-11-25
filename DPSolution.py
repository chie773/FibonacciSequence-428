# Time Complexity: O(n)
# Space Complexity: O(n) 
# Drawbacks:
# 1) The bottom-up methods stores all values from 0 to n, so it is wasteful for large n values
# 2) It cannot skip intermediate results and has to compute every Fibonacci number to n

def fib_dp(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    print(fib_dp(10))
 