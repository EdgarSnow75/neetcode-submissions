"""
So I need to find the value where the lower one of two heights multiplied by the distance between the two bars is the highest

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            current_area = 0
            if heights[i] >= heights[j]:
                current_area = heights[j] * (j - i)
                j -= 1
            elif heights[i] <= heights[j]:
                current_area = heights[i] * (j - i)
                i += 1
            if current_area > max_area:
                max_area = current_area
        return max_area

        