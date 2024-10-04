#3. Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s):
        # Dictionary to store the last seen index of each character
        char_index_map = {}
        max_len = 0
        left = 0  # Left pointer of the sliding window
        
        # Iterate through the string with the right pointer
        for right, char in enumerate(s):
            # If the character is already in the window, move the left pointer
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1
            
            # Update the last seen index of the character
            char_index_map[char] = right
            
            # Update the maximum length
            max_len = max(max_len, right - left + 1)
        
        return max_len
