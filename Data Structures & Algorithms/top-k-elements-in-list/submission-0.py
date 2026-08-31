class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kMap = {}
        result = []
        n = len(nums)
        for num in nums:
            kMap[num] = kMap.get(num, 0) + 1
        
        #for i in range(n):
            #result.append(max(kMap.values()))
            #del kMap[max(kMap.values())]

        while len(result) < k:
            max_val = max(kMap.values())
            for key in list(kMap.keys()):
                if kMap[key] == max_val:
                    result.append(key)
                    del kMap[key]
                    break

        return result