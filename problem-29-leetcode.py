#29. Divide Two Integers

class Solution:
    def divide(self, dividend, divisor):
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Return 2^31 - 1 to prevent overflow

        # Determine the sign of the quotient
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0

        # Perform the division using bit manipulation
        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):  # Left shift temp
                temp <<= 1
                multiple <<= 1

            # Subtract the largest shifted divisor from dividend
            a -= temp
            quotient += multiple

        # Apply the sign to the quotient
        if negative:
            quotient = -quotient

        return quotient

# Example usage
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    dividend1 = 10
    divisor1 = 3
    print(sol.divide(dividend1, divisor1))  # Output: 3

    # Test case 2
    dividend2 = 7
    divisor2 = -3
    print(sol.divide(dividend2, divisor2))  # Output: -2
