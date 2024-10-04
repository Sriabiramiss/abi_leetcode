#18. 4Sum

class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Sort the input array
        n = len(nums)
        quadruplets = set()  # Use a set to avoid duplicates

        for i in range(n):
            for j in range(i + 1, n):
                left, right = j + 1, n - 1  # Initialize two pointers

                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        # Found a quadruplet
                        quadruplets.add((nums[i], nums[j], nums[left], nums[right]))

                        left += 1
                        right -= 1

                        # Skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif current_sum < target:
                        left += 1  # Move left pointer to increase the sum
                    else:
                        right -= 1  # Move right pointer to decrease the sum

                # Skip duplicates for the second index
                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1

            # Skip duplicates for the first index
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1

        return [list(quadruplet) for quadruplet in quadruplets]  # Convert set to list for the result
