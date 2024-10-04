#8. String to Integer (atoi)



class Solution:
    def myAtoi(self, s):
        # Define 32-bit signed integer limits
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # Step 1: Ignore leading whitespace
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check if the next character is '-' or '+'
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1
        
        # Step 3: Read the digits and convert to integer
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow and underflow before updating the result
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        # Step 4: Apply the sign and return the result
        return result * sign
