class Solution:
    '''
    U: return the indices in which num[i] + num[j] = target
    P:
        1. hash_set
        2. loop thorough nums -> i
        3. compliment = target - num[i]
        4. is the nums[i] in our hash_set: return[hash_set[compliment],i] 
        5. hash_set[compliment] = i
        6. return []

        nums = [3,4,5,6], target = 7
            hash_set= { 4:0, 3:1, 2:2, 1:3}
         nums = [3,4,3], target = 6
          hash_set= {3:0, 4:1}
    I:
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if nums[i] in hash_set:
                return [hash_set[nums[i]], i]
            
            hash_set[compliment] = i
        
        return []



        