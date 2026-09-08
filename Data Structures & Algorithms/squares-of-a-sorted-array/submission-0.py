class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        for j in range(len(nums)):
            smallest_num = nums[j]
            smallest_index = j
            for k in range(j + 1, len(nums)):
                current_num = nums[k]
                if current_num < smallest_num:
                    smallest_num = current_num
                    smallest_index = k
            temp_num = nums[j]
            nums[j] = smallest_num
            nums[smallest_index] = temp_num

        return nums
            

            
        
        