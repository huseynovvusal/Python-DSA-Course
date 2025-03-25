from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]

        for curr in nums[1:]:
            idx = bisect_left(res,curr)

            if(idx == len(res)):
                res.append(curr)
            else:
                res[idx] = curr

        return len(res)


    def lower_bound(self, arr, target):
        l = 0
        r = len(arr)

        while(l < r):
            mid = (l + r) // 2

            if(target > arr[mid]):
                l = mid + 1
            else:
                r = mid

        return l

s = Solution()
print(s.lower_bound([2,5,10,20,35,40,60,120], 130))