class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        sorted_nums = []
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                sorted_nums.append(nums[l] * nums[l])
                l += 1
            else:
                sorted_nums.append(nums[r] * nums[r])
                r -= 1
        return sorted_nums[::-1]


            


            

            
        
        