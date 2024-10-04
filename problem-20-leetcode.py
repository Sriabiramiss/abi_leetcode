#20. Valid Parentheses

class Solution:
    def isValid(self, s):
        # Dictionary to hold matching pairs
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the topmost element if the stack is not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched correctly
        return not stack
