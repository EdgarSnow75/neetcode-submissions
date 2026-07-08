class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, 1
        while (numbers[i] + numbers[j]) != target:
            if i < j and j < (len(numbers) - 1):
                j += 1
            elif j == (len(numbers) - 1):
                i += 1
                j = i + 1
        return [i + 1, j + 1]
        
            

        