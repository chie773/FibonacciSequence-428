# Time Complexity: O(2^n)
# Reason: each call generates two more calls (binary recursion tree)
# Space Complexity: O(n) call stack depth
# Drawbacks:
# 1) explodes exponentially for inputs above 45
# 2) repeats subproblems many times, such as fib(38)

class RecFib:

    @staticmethod
    def fib_recursive(n, depth=0):
        RecFib.visualize_call(n, depth)

        if n <= 1:
            RecFib.visualize_return(n, depth)
            return n

        result = RecFib.fib_recursive(n - 1, depth + 1) + RecFib.fib_recursive(n - 2, depth + 1)

        RecFib.visualize_return(result, depth)
        return result

    @staticmethod
    def visualize_call(n, depth):
        indent = "  " * depth
        print(f"{indent}Calling fib({n})")

    @staticmethod
    def visualize_return(value, depth):
        indent = "  " * depth
        print(f"{indent}Returning {value}")

