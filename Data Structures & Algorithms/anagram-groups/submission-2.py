class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
        # key_map = {}
        # for item in strs:
        #     key = "".join(sorted(item))
        #     if key in key_map:
        #         key_map[key].append(item)
        #     else:
        #         key_map[key] = [item]
        # return list(key_map.values())
            

        
        