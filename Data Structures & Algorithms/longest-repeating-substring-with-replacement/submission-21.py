class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chara_hash = {}
        max_len = 0
        l = 0
        for r in range(len(s)): 
            chara_hash[s[r]] = chara_hash.get(s[r], 0) + 1 
            highest_freq_chara = max(chara_hash.values())
            while ((r - l) + 1) - highest_freq_chara > k:
                chara_hash[s[l]] -= 1
                l += 1 
            max_len = max(max_len, (r - l) + 1) 
        return max_len

        



