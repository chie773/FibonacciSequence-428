# Time Complexity: O(2^n)
# Reason: each call generates two more calls (binary recursion tree)
# Space Complexity: O(n) call stack depth
# Drawbacks: 
# 1) explodes exponentially for inputs above 45
# 2) repeats subproblems many times, such as fib(38)

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


if __name__ == "__main__":
    print(fib_recursive(10))

