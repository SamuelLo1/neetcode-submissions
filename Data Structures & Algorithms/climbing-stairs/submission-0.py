class Solution:
    def climbStairs(self, n: int) -> int:
        counter = 0

        # dfs code
        def dfs(i):
            nonlocal counter  # Refer to the counter from the enclosing scope
            if i == n:
                counter += 1
            elif i > n:
                return
            else:
                dfs(i + 1)
                dfs(i + 2)

        dfs(0)
        return counter