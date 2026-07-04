'''
inputs: array of integers 

cost[i] is the cost of taking a step from the ith floor of a staircase
    - past the last index 
After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

    - can devise a problem to get the minimum cost between (i + 1) and (i + 2)
    - decision tree
    - either i + 1, or i + 2   

You may choose to start at the index 0 or the index 1 floor.

    - going backwards? 
Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.


Observe: 

- cost lenght med
- cost cannot be negative
    - there cant be negative output cost

example: 
    costs: [1,2,3]
            3 2 3

    costs: [1,2,1,2,1,1,1]
            4,5,3,3,2,1,1


- reverse loop through costs
- for each index, populate a dp arr
- for each index, get the previous 2 elements and get the min and add on for current index
- return the minimum of dp[0] and dp[1]
    

'''



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0] * (len(cost))

        #dp's last 2 elements should not change
        dp[len(cost) - 1] = cost[len(cost) - 1] 
        dp[len(cost) - 2] = cost[len(cost) - 2]

        for i in range(len(cost) - 3, -1, -1):
            minimumCost = min(dp[i + 1], dp[i + 2])
            dp[i] = cost[i] + minimumCost


        return min(dp[0], dp[1])

        
        