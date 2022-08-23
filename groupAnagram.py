from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Using a hashmap we will step through each word and set the key as the letters sorted
        append each word that has the same sorted letters. 
        Afterwards, return the sorted list of values
        """
        anagram_groups = {}
        for s in strs:
            res = ''.join(sorted(s))  # join the sorted chars
            if res in anagram_groups:
                # if sorted char sequence exists then append curr word
                anagram_groups[res].append(s)
            else:
                anagram_groups[res] = [s]  # else start the collection
        # return a list sorted by lengths
        return list(sorted(anagram_groups.values(), key=lambda x: len(x)))


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
