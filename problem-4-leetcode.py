#4. Median of Two Sorted Arrays


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array for binary search on it
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            # Check if i is too small (we need to move right)
            if i < m and nums2[j - 1] > nums1[i]:
                left = i + 1
            # Check if i is too large (we need to move left)
            elif i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                # Found the correct partition
                # Handle edge cases for max of left side
                if i == 0: left_max = nums2[j - 1]
                elif j == 0: left_max = nums1[i - 1]
                else: left_max = max(nums1[i - 1], nums2[j - 1])
                
                # If odd, return max of left side
                if (m + n) % 2 == 1:
                    return left_max
                
                # Handle edge cases for min of right side
                if i == m: right_min = nums2[j]
                elif j == n: right_min = nums1[i]
                else: right_min = min(nums1[i], nums2[j])
                
                # If even, return the average of the two middle values
                return (left_max + right_min) / 2.0
