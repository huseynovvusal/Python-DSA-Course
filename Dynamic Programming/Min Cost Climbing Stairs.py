from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        one = cost[0]
        two = cost[1]

        if(n <= 2): return min(one, two)

        for i in range(2,n):
            curr_cost = cost[i] + min(one,two)

            one = two
            two = curr_cost

        return min(one,two)
