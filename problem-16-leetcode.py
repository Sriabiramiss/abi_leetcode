#16. 3Sum Closest



class Solution:
    def threeSumClosest(self, nums, target):  # Removed type hints
        nums.sort()  # Sort the array first
        closest_sum = float('inf')  # Start with a very large number
        
        for i in range(len(nums) - 2):  # Iterate over the array
            left, right = i + 1, len(nums) - 1  # Set left and right pointers
            
            while left < right:  # While pointers do not cross
                current_sum = nums[i] + nums[left] + nums[right]  # Calculate current sum
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison with the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Exact match found

        return closest_sum  # Return the closest sum found
