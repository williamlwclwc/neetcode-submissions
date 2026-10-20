class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur, count = nums[0], 1
        for i in range(1, len(nums)):
            if cur == nums[i]:
                count += 1
            else:
                count -= 1
                if count == -1:
                    cur = nums[i]
                    count = 1
        return cur

