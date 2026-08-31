from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listT = list(t)
        if len(s) != len(t):
            return False
        if Counter(s) != Counter(t):
            return False
        return True