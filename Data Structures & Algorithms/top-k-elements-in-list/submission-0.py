class Solution:
    '''
    U: return the k most frequent element within the array
    P:
        1. we need to find the frequency of all numbers in the array
        2. sort the values in descending order --> figure out a way to get k elements
        3. loop through the dictionary
        4. if dict[key] in sorted_list of k elemnets: append(key) 
        5. return key
    I:
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}
        topK = []

        for key in nums:
            if key in freq_map:
                freq_map[key] += 1
                continue
            freq_map[key] = 1
        
        klist = list(sorted(freq_map.values(), reverse=True))
        klist = set(klist[:k])

        for key in freq_map:
            if freq_map[key] in klist:
                topK.append(key)
        
        return topK
            
        