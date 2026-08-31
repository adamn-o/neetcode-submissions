class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = Counter(nums)
        result = [i[0] for i in num.most_common(k)]
        return result