# Fibonacci Sequence

ihab update cooked

This project is cooked

This project is an in depth analysis of a very common Dynamic Programming problem that many cs majors encounter within the early stages of their tech journey, **Fibonacci Sequence**.


 - The *Fibonacci sequence* is a recursively defined numerical progression in which each term is computed as the sum of its two immediate predecessors, establishing a well-structured recurrence relation. This formulation inherently exhibits overlapping subproblems, as the computation of higher-indexed terms repeatedly depends on identical lower-indexed subcomputations. It also demonstrates optimal substructure, since the solution to the overall recurrence is optimally derived from the solutions to its constituent subproblems. These properties make the Fibonacci sequence a canonical use case for Dynamic Programming (DP). By leveraging memoization or tabulation, DP transforms the naïve exponential-time recurrence into a deterministic, polynomial-time computation through systematic state caching or iterative state propagation. Moreover, the recurrence can be further optimized using constant-space DP techniques, emphasizing DP’s role in eliminating redundant computations, minimizing time complexity, and enforcing predictable computational constraints within recursive numerical systems.

## Installation

### Clone the repository:

`git clone https://github.com/chie773/FibonacciSequence-428`

`cd FibonacciSequence-428`



## Usage

### Depending on your which solution you want to access, you may run the Fibonacci program using:

Command Line  

`python RecursiveSolution.py`  

`python DPSolution.py`

## Algorithm Overview

* Recurrence Relation:

    * 𝐹(𝑛) = 𝐹(𝑛 − 1) + 𝐹(𝑛 − 2)

* DP Optimization:

    * Eliminates redundant recomputation

    * Uses memoization, tabulation, or constant-space iteration

    * Converts exponential *𝑂(2𝑛)* time complexity into linear *𝑂(𝑛)*

## Complexity Analysis

| Approach               | Time Complexity | Space Complexity |
| ---------------------- | --------------- | ---------------- |
| Naïve Recursion        | ( O(2^n) )      | ( O(n) ) (stack) |
| Memoization (Top-Down) | ( O(n) )        | ( O(n) )         |
| Tabulation (Bottom-Up) | ( O(n) )        | ( O(n) )         |
| Space-Optimized DP     | ( O(n) )        | ( O(1) )         |


## Video Demonstration
https://github.com/user-attachments/assets/03da845f-ba28-4774-ad7d-b09adcd2aed4




