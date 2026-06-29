class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        modified_int_list = []
        for i in range(len(nums)):
            product_num = 1
            for k in range(len(nums)):
                if k != i:
                    product_num *= nums[k]
            modified_int_list.append(product_num)
        return modified_int_list
                

                
        