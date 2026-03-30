# s and t 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap_S = {}
        hashmap_T = {}
        for i in range(len(s)):
            hashmap_S[s[i]] = 1 + hashmap_S.get(s[i], 0)
            hashmap_T[t[i]] = 1 + hashmap_T.get(t[i], 0)
        for c in hashmap_S:
            if hashmap_S[c] != hashmap_T.get(c,0):
                return False
        return True
#sorting 
       #  return sorted(s) == sorted(t) 
