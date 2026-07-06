class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_string = ''.join(l for l in s if l.isalnum()).lower()
        length_of_string = len(normalized_string)
        first_half = ""
        second_half = ""
        mid_point = length_of_string // 2

        if length_of_string % 2 != 0:
            first_half = normalized_string[:mid_point]
            second_half = normalized_string[mid_point + 1:]
        else:
            first_half = normalized_string[:mid_point]
            second_half = normalized_string[mid_point:]

        if len(first_half) != len(second_half):
            return False

        for i in range(len(first_half)):
            if first_half[i] != second_half[len(second_half) - (i + 1)]:
                return False
        
        return True



            



        