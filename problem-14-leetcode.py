#14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            while not s.startswith(prefix):  # While the string doesn't start with the prefix
                prefix = prefix[:-1]  # Shorten the prefix by one character
                if not prefix:  # If the prefix becomes empty, return ""
                    return ""
        
        return prefix
        
