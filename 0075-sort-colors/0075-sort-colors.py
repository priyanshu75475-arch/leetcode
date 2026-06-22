class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap current 0 into the low boundary
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 belongs in the middle, just move forward
                mid += 1
            else: # nums[mid] == 2
                # Swap current 2 into the high boundary
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1