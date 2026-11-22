class Solution:
    '''
    U:
            Two str --> anagram T/F
    P:
        1. if len not the same: False
        2. sort both strings
        3. loop
        4. if sort1 != sort2: return false
        5. return true
    I:
        s = "racecar", t = "carrace"
        "aaccerr"  "aaccerr"




        s = "jar", t = "jam"
        "ajr" "ajm"


    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sort1, sort2 = sorted(s), sorted(t)
        
        return sort1 == sort2
        