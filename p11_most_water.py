from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for i in range(n):
            for j in range(i+1, n):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area

class Solution1:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        h = height
        start = 0
        end = 1
        max_area = min(h[start], h[end])
        for i in range(2, n):
            area = i * min(h[start], h[i])
            if  area > max_area:
                end = i
                max_area = area
                print("new end", end)
        for i in range(0, end):
            area = (end - i) * min(h[i], h[end])
            if  area > max_area:
                start = i
                max_area = area
                print("new start", start)
        return max_area



sol = Solution1()

print(sol.maxArea([2,3,4,5,18,17,6]))