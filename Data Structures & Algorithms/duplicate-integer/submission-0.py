class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bin = []
        result = False
        for num in nums:
            if num in bin:
                result = True
            bin.append(num)
        return result