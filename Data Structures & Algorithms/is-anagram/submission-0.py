# s and t 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    # set 2 hashmaps one for each string, and add the count of each letter in the string
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # for looping through length of s as s and t are both the same length
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        #iterate through hashmap to make sure counts are same    
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
