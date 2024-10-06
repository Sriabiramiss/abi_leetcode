#30. Substring with Concatenation of All Words

from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        
        # Create a Counter for the words
        word_count = Counter(words)
        
        indices = []
        
        # Iterate through the string s with a sliding window
        for i in range(len(s) - total_length + 1):
            # Extract the current substring
            current_substring = s[i:i + total_length]
            
            # Split the substring into words of equal length
            split_words = [current_substring[j:j + word_length] for j in range(0, total_length, word_length)]
            
            # Create a Counter for the split words
            current_count = Counter(split_words)
            
            # Compare the current word count with the original word count
            if current_count == word_count:
                indices.append(i)

        return indices
