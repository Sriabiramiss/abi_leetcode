#6. Zigzag Conversion

class Solution:
    def convert(self, s, numRows):
        # If there is only one row, return the original string
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of strings to hold the characters of each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Place characters in the appropriate row
        for char in s:
            rows[current_row] += char
            # Change direction when we hit the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move to the next row
            current_row += 1 if going_down else -1
        
        # Concatenate all rows and return the result
        return ''.join(rows)
