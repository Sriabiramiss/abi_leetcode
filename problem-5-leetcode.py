#5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s):
        if not s or len(s) == 0:
            return ""
        
        start, end = 0, 0
        
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            # Check for odd-length palindromes (single center)
            len1 = expandAroundCenter(s, i, i)
            # Check for even-length palindromes (two centers)
            len2 = expandAroundCenter(s, i, i + 1)
            # Get the maximum length
            max_len = max(len1, len2)
            
            # Update start and end if a longer palindrome is found
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        # Return the longest palindromic substring
        return s[start:end + 1]
