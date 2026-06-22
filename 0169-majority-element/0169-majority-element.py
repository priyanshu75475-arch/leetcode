class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # If count drops to 0, choose the current element as the new candidate
            if count == 0:
                candidate = num
            
            # Add 1 if num matches candidate, subtract 1 if it doesn't
            count += 1 if num == candidate else -1
            
        return candidate
        