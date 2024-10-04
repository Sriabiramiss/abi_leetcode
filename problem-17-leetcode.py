#17. Letter Combinations of a Phone Number


class Solution:
    def letterCombinations(self, digits):
        if not digits:  # Return empty list if input is empty
            return []
        
        # Mapping from digit to corresponding letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []  # List to hold the results
        
        def backtrack(index, path):
            if index == len(digits):  # If the current combination is done
                result.append(path)  # Add the combination to the result
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            letters = digit_to_letters[current_digit]
            
            for letter in letters:  # Loop through the letters
                backtrack(index + 1, path + letter)  # Recurse with the next index
        
        backtrack(0, "")  # Start the backtracking process
        return result  # Return the list of combinations
