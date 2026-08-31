class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        check = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            check = max(area, check)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return check