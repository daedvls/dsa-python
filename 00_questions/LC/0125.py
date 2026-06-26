# https://leetcode.com/problems/valid-palindrome/description/

'''
New thing here:
str.isalpha() -> returns true if str contains ONLY alphabet chars. False if even a single space or symbol or num
str.isalnum() -> returns true if str contains ONLY alphanumeric chars.

'''

str = "A man, a plan, a canal: Panama"
arr = [char.lower() for char in str if char.isalnum()]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [char.lower() for char in s if char.isalpha()]
        for i in range(len(arr)//2):
            if arr[i]!=arr[len(arr)-1-i]:
                return False
        return True