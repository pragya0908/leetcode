class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Dictionary to store the last seen index of each character
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If the character is in the map and within our current sliding window
            if s[right] in char_map and char_map[s[right]] >= left:
                # Move the left pointer past the previous occurrence of this character
                left = char_map[s[right]] + 1
            
            # Record/update the position of the current character
            char_map[s[right]] = right
            
            # Calculate the window size and update the maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length