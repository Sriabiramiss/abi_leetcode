#13. Roman to Integer

class Solution:
    def romanToInt(self, s):
        # Define the Roman numeral symbols and their integer values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate over each character in the string
        for char in reversed(s):
            current_value = roman_values[char]
            # If the current value is less than the previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            # Update the previous value for the next iteration
            prev_value = current_value
            
        return total
        
