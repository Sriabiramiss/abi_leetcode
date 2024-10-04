#9. Palindrome Number

class Solution:
    def isPalindrome(self, x):
        # Step 1: Handle negative numbers and numbers ending in 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # Step 2: Reverse the second half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Step 3: Compare the first half and the reversed second half
        # For odd number of digits, we need to divide reversed_half by 10
        return x == reversed_half or x == reversed_half // 10
