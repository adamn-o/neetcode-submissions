class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pripix = [0] * length
        supix = [0] * length
        result = [0] * length

        pripix[0] = 1
        supix[length - 1] = 1
        for i in range(1, length):
            pripix[i] = nums[i - 1] * pripix[i - 1]

        """1000 p
	    0100 s

	    1000"""


        for i in range(length-2, -1, -1):
            supix[i] = nums[i + 1] * supix[i + 1]

        for i in range(length):
            result[i] = pripix[i] * supix[i]
        return result