#22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n):
        result = []
        
        def backtrack(current, open_count, close_count):
            # If the current string is of the maximum length, add it to the results
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an opening parenthesis if we still have some left
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # Add a closing parenthesis if it won't exceed the number of opening parentheses
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        # Start the backtracking process
        backtrack('', 0, 0)
        return result
