class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums2 = [i for i in nums]
        for i in range(n):
            nums2[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = nums2[i]