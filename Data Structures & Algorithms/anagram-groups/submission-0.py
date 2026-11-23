class Solution:
    '''
    U: given an array group all anagrams together into a sublist
    P:
        1. create a dict
        2. loop through all words
        3. sort each word and use it as a key
        4. if key not in group: group[key] = []
        5. group[key].append(wrd)
        6. return list(group.values)
    I:
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for wrd in strs:
            key = "".join(sorted(wrd))

            if key not in group:
                group[key] = []
            
            group[key].append(wrd)
        
        return list(group.values())

