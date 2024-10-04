#1. Two Sum

class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store the number and its index
        num_to_index = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if complement is in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Add the current number and its index to the dictionary
            num_to_index[num] = i
