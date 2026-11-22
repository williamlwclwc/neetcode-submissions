class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, left, right = 0, 0, len(people)-1
        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            res += 1
        if left == right:
            res += 1
        return res