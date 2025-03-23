class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        l = r = 0
        res = 0

        while(l <= r < len(s)):
            new_char = s[r]

            if(new_char in window):
                window.remove(s[l])
                l += 1
            else:
                window.add(new_char)
                r += 1

            res = max(res,len(window))

        return res

solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))