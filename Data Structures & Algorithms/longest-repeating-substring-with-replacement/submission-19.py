"""
The longest repeating substring should be either the entire len(s) or it should be the most frequent character length plus either k or (len(s) - most freq chara len) whichever is smaller

Using a hash map, we can map each character to their word frequency 
Out of that, pick the most frequent character 
Check if k is greater than the remaining length of the string after deducing the highest freq charac 
    If so, that would mean k has more than enough replacements and the longest substring without repeats is just length of the string
    So return the length of the string

We need to define the sliding window length first. It should be checked if whether len(s) is smaller than highest_freq + k cause we should just return len(s) if that is the case. 
First, let's set the max_len to 0
Using the two pointers, we go from start to end but this time, we only need to account how much we can move the left pointer, 
Start the left pointer at 0 and set right pointer to highest_freq + k 
Try to replace all the characters in the substring k times 
Go through the substring and calculate the current_len
If current_len > max_len,
    Set max_len to current_len
Repeat this until r is at len(s)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chara_hash = {}
        max_len = 0
        l = 0
        for r in range(len(s)): # The right pointer starts at 0 and grows
            chara_hash[s[r]] = chara_hash.get(s[r], 0) + 1 # For each character, increment that character count by 1
            highest_freq_chara = max(chara_hash.values()) #Calculate the highest freq chara in the current window
            while ((r - l) + 1) - highest_freq_chara > k: # Check if the remaining characters of the window minus the highest freq character is less than k since we can only handle at most k characters that are different from the most frequent character in the window/substring
                chara_hash[s[l]] -= 1 #Remove the leftmost character of the substring
                l += 1 #Narrow the window size by shifting the left pointer to the right
            max_len = max(max_len, (r - l) + 1) #Check if the max_len is less than the current length of the valid window l + r, if so, set max_len to l+r - 1
        return max_len

        



