#27. Remove Element

class Solution:
    def removeElement(self, nums, val):
        # Initialize the count of elements that are not equal to val
        k = 0
        
        # Traverse the array
        for i in range(len(nums)):
            if nums[i] != val:
                # Place the non-val element at the k-th position
                nums[k] = nums[i]
                k += 1
                
        # Return the count of non-val elements
        return k

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = sol.removeElement(nums1, val1)
    print(k1)              # Output: 2
    print(nums1[:k1])     # Output: [2, 2]
    
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = sol.removeElement(nums2, val2)
    print(k2)             # Output: 5
    print(nums2[:k2])     # Output: [0, 1, 3, 0, 4]
