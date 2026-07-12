class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_list = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = i + 1
            j = len(nums) - 1
            while k < j:
                triplet_sum = nums[i] + nums[k] + nums[j]
                if triplet_sum > 0 and j > i:
                    j -= 1
                elif triplet_sum < 0 and k < j:
                    k += 1
                else:
                    entry_list = [nums[i], nums[k], nums[j]]
                    if entry_list not in triplet_list:
                        triplet_list.append(entry_list)
                    k += 1
                    j -= 1
        return triplet_list
