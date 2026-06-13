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
        """
        Set the modified array to the same length as nums by filling up with 1s
        Since we need to set the out-of-bound prefix, set the prefix to be 1
        Loop until we reach the length of the nums array
            Firstly, we set the modified array's current iteration to be the prefix num
            Second, we update the prefix number by multiplying it with the corresponding number in nums
            We do this until we get all the prefixes in the modified array minus the last one since its all prefixes
        We then set the postfix number to be 1 to account for the initially out-of-bounds post-fix num
        Loop from the end of the array to the first in a reverse order
            Firstly, we set the the modified array's current iteration to be the product of the current postfix number and the current iteration (Essentially prefix * postfix)
            Secondly, we update the postfix number by multiplying it with the corresponding number in nums
        """
        modified_int_list = [1] * (len(nums))
        prefix_num = 1
        for i in range(len(nums)):
            modified_int_list[i] = prefix_num
            prefix_num *= nums[i]
        post_fix_num = 1
        for j in range(len(nums) - 1, -1, -1):
            modified_int_list[j] *= post_fix_num
            post_fix_num *= nums[j]
        return modified_int_list
        # modified_int_list = []
        # for i in range(len(nums)):
        #     product_num = 1
        #     for k in range(len(nums)):
        #         if k != i:
        #             product_num *= nums[k]
        #     modified_int_list.append(product_num)
        # return modified_int_list
                
        