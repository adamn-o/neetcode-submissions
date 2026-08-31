from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagMap = defaultdict(list)
        store = []
        n = len(strs)
        for str in strs:
            sorted_strs = ''.join(sorted(str))
            anagMap[sorted_strs].append(str)

        for v in anagMap.values():
            store.append(v)
        
        return store