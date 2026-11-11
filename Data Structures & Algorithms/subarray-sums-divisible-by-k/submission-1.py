class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix, res = 0, 0
        for i, num in enumerate(nums):
            prefix += num
            res += count[prefix % k]
            count[prefix % k] += 1
        return res