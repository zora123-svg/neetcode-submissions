'''
U: determine if an array contains dupliates --> T/F
P:
    1. create a set and put the list in the set
    2. then campare the length of the set with the length of the list
    3. if equal return false else if not equal return true
I:
    nums[1, 2, 3, 3]   set[1, 2, 3]
    Edges: empty list --> 
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = set(nums)

        if len(nums) == len(isDuplicate):
            return False
        return True
        