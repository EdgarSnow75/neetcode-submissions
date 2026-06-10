class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Create a list called anagram_sublists with the first element of the original list added as a list
        Loop through the original list from the second item
            Loop through the new list using an inner loop
                If the length of the two items are not the same
                    add the current iteration's item to the new list as a list
                If same, using sorted, check if they are anagrams,
                    If so, add the new item to the inner loop item's list
                    If not, add the current iteration's item to the new list as a list
        Return the anagram_sublists
        """
        anagram_sublists = [[strs[0]]]
        for j in range(1, len(strs)):
            item = strs[j]
            for i in range(len(anagram_sublists)):
                inner_item = anagram_sublists[i][0]
                if sorted(item) == sorted(inner_item):
                    anagram_sublists[i].append(item)
                    break
                elif (i + 1 == len(anagram_sublists)):
                    anagram_sublists.append([item])
        return anagram_sublists
        
        