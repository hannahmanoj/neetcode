class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''count = {} # to count and map the number of occurences of each value
        freq = [[] for i in range(len(nums) + 1)] # [1,2,2,2,3,3]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res'''

        
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # index will be frequency of element and num will be the val
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res