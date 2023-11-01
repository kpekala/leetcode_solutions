from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        zero_n = len([num for num in nums if num == 0])
        print(zero_n)
        for i in range(n):
            while nums[i] == 0 and i < n-zero_n:
                for j in range(i, n-1):
                    nums[j], nums[j+1] = nums[j+1], nums[j]



sol = Solution()
x = [0,1,0]
sol.moveZeroes(x)
print(x)

        
        
        