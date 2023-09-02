from typing import List

# Accepted
# Runtime beats 5.00% of users with Python3
# Memory beats 11.97% of users with Python3
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = []
        m = {}
        for i in range(n):
            if nums[i] not in m:
                m[nums[i]] = 0
            m[nums[i]] += 1
        for i in range(n):
            if nums[i] > 0:
                break
            for j in range(i+1, n):
                x = nums[i]
                y = nums[j]
                a = x+y
                if a > 0 :
                    break
                if -a in m and not (-a == x or -a ==y and m[-a] < 2) or (x == 0 and y == 0 and m[0] > 2):
                    xs = sorted([x, y, -a])
                    if xs not in res:
                        res.append(xs)
        return res
    
sol = Solution()