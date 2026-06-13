class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Set an empty int list named modified_int_list 
        Loop through the nums list as an outer loop
            Set an int variable named product_num to 1
            Loop through the nums list again as an inner loop
                if the inner iteration is not equal to the outer iteration index:
                    Update the product_num by multipying it with the inner iteration num
            Append the product_num to the modified_int_list
        """
        modified_int_list = []
        for i in range(len(nums)):
            product_num = 1
            for k in range(len(nums)):
                if k != i:
                    product_num *= nums[k]
            modified_int_list.append(product_num)
        return modified_int_list
                
        