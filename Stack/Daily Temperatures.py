from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # (temp, index)
    stack = []
    res = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while(stack and t > stack[-1][0]):
            temp, index = stack.pop()

            res[index] = i - index

        stack.append((t, i))

    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))