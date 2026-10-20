class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        prefix, res = 0, 0
        for i, num in enumerate(nums):
            prefix += 1 if num == 1 else -1
            if prefix in first:
                res = max(res, i - first[prefix])
            else:
                first[prefix] = i
        return res

