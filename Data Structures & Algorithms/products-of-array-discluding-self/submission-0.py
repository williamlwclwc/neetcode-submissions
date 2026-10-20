class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, n = 1, len(nums)
        res = [1] * len(nums)
        for i in range(n-2, -1, -1):
            res[i] = res[i+1] * nums[i+1]
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        return res 