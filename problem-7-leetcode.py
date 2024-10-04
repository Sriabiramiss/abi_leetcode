#7. Reverse Integer


class Solution:
    def reverse(self, x):
        # Define the 32-bit signed integer range
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # Store the sign and make x positive for easier manipulation
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Initialize the reversed number
        reversed_num = 0
        
        while x != 0:
            # Extract the last digit of x
            pop = x % 10
            x //= 10
            
            # Check for overflow/underflow before adding the digit
            if (reversed_num > INT_MAX // 10) or (reversed_num == INT_MAX // 10 and pop > 7):
                return 0  # Overflow
            if (reversed_num < INT_MIN // 10) or (reversed_num == INT_MIN // 10 and pop > 8):
                return 0  # Underflow
            
            # Build the reversed number
            reversed_num = reversed_num * 10 + pop
        
        # Return the reversed number with the original sign
        return sign * reversed_num
