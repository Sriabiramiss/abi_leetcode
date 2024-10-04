#12. Integer to Roman

class Solution:
    def intToRoman(self, num) :
        # Define the Roman numeral symbols and their values
        roman_numerals = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]
        
        # Initialize an empty result string
        result = ""
        
        # Iterate through each symbol-value pair
        for symbol, value in roman_numerals:
            # While the number is greater than or equal to the value,
            # append the symbol to the result and subtract the value from the number
            while num >= value:
                result += symbol
                num -= value
        
        # Return the resulting Roman numeral
        return result
