#26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums):
        # Edge case: if the list is empty, return 0
        if not nums:
            return 0
        
        # Initialize the second pointer (j) to track unique elements
        j = 1
        
        # Traverse the array starting from the second element
        for i in range(1, len(nums)):
            # If a new unique element is found
            if nums[i] != nums[i - 1]:
                # Place it at the j-th position
                nums[j] = nums[i]
                j += 1
        
        # Return the number of unique elements
        return j

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    print(k)           # Output: 2
    print(nums[:k])   # Output: [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print(k2)         # Output: 5
    print(nums2[:k2]) # Output: [0, 1, 2, 3, 4]
