#28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack , needle):
        # If needle is an empty string, return 0
        if not needle:
            return 0
        
        needle_length = len(needle)
        haystack_length = len(haystack)

        # Loop through the haystack
        for i in range(haystack_length - needle_length + 1):
            # Check if the substring from i matches the needle
            if haystack[i:i + needle_length] == needle:
                return i  # Return the starting index of the first occurrence

        return -1  # Return -1 if needle is not found
