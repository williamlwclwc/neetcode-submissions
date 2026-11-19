class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, i = 0, n-1, n-1
        res = [0] * n
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res[i] = nums[left] * nums[left]
                left += 1
            else:
                res[i] = nums[right] * nums[right]
                right -= 1
            i -= 1
        return res
