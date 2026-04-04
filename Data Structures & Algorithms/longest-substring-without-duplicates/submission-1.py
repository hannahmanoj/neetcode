class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window problem 
        #
        charSet = set()
        #left pointer initialised to 0
        L = 0
        #longest length
        res = 0

        # right pointer is going to continuously change as we visit every character
        for R in range(len(s)):
            #if we get a duplicate character then we have to update our window and our set 
            while s[R] in charSet: #meaning its a duplicate 
                charSet.remove(s[L]) #take the left character and remove it from the set
                L += 1 #update the left pointer
            charSet.add(s[R]) #add the right most character to the set
            res = max(res, R - L + 1) #
        return res
