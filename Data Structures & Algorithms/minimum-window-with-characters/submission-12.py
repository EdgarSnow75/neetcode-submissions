"""

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tempt_t = {}
        tempt_s = {}
        for word in t:
            tempt_t[word] = tempt_t.get(word, 0) + 1
        valid_len = 0
        real_l = 0
        l = 0
        for r in range(len(s)):
            if s[r] in tempt_t:
                tempt_s[s[r]] = tempt_s.get(s[r], 0) + 1 
                while self.check_validity(tempt_t, tempt_s):
                    if valid_len == 0 or r - l + 1 < valid_len:
                        real_l = l
                        valid_len = r - l + 1
                    if s[l] in tempt_s:
                        tempt_s[s[l]] -= 1
                    l += 1
        return s[real_l:real_l + valid_len] if valid_len != 0 else ""

    def check_validity(self, tempt_t, tempt_s):
        for word in tempt_t:
            if tempt_t[word] > tempt_s.get(word, 0):
                return False
        return True



        