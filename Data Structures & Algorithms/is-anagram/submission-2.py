class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        for c in t:
            if c not in m:
                return False
            m[c] -= 1
            if m[c] == 0:
                m.pop(c)
        if len(m) == 0:
            return True
        else:
            return False
