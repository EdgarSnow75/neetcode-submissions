class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for letter in t:
            if letter in s:
                s = s.replace(letter, "", count = 1)
                t = t.replace(letter, "", count = 1)
        if t == "" and s == "":
            return True
        return False

        