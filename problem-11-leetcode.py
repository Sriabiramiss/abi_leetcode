#11. Container With Most Water

class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        # Use the two-pointer approach
        while left < right:
            # Calculate the area between the two lines
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            # Move the pointer at the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        
