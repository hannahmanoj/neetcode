class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we'll use a hashmap - key : value where the key would be pattern of string and val would be the list of strings that match the pattern in the key
        #time complex: O(m.n) where m is the total number of input string that we're given and n is the average length of a string because we have to count how many letters it has so we go through every single char in the string
        #space: O(n)
        from collections import defaultdict

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())
