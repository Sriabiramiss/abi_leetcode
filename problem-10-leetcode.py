#10. Regular Expression Matching


class Solution:
    def isMatch(self, s, p):
        # Create a DP table with size (len(s) + 1) x (len(p) + 1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty string and empty pattern is a match
        dp[0][0] = True
        
        # Handle patterns like "a*", "a*b*", ".*", etc. at the start
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    # If characters match or if there's a '.'
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # Two cases for '*'
                    # Case 1: Zero occurrences of the preceding character
                    dp[i][j] = dp[i][j-2]
                    # Case 2: If preceding character matches or if it's '.'
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        
        # The answer is whether the full string s matches the full pattern p
        return dp[len(s)][len(p)]
