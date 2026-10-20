class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        s, res = 0, 0
        for i, num in enumerate(nums):
            s += num
            res += prefix[s % k]
            prefix[s % k] += 1
        return res