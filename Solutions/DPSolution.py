class DPS:
    def fib_dp(n):
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        DPS.visualize_step(dp, step=1)

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            DPS.visualize_step(dp, step=i)

        return dp[n]

    @staticmethod
    def visualize_step(dp, step):
        print(f"Step {step}: {dp}")
