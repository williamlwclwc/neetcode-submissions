class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        s, res = 0, 0
        for i in range(len(nums)):
            s += nums[i]
            # check first, save later
            res += prefix[s - k]
            prefix[s] += 1
        return res