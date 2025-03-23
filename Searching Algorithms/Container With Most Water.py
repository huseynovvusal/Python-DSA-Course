from typing import List

def maxArea(arr: List[int]) -> int:
    l = 0
    r = len(arr) - 1
    m = 0

    while(l < r):
        if(arr[l] > arr[r]):
            m = max(m,arr[r] * (r - l))
            r -= 1
        else:
            m = max(m,arr[l] * (r - l))
            l += 1
            
    return m