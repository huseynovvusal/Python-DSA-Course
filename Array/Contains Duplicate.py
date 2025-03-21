from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()

    for i in range(1,len(nums)):
        if(nums[i] == nums[i - 1]): return True

    return False

print(containsDuplicate([1,2,3,4,5,5]))