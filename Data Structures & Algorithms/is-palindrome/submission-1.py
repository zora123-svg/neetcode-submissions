class Solution:
    '''
    U: return true if a string is a palindrome
    P:
        1. create a variable called palindrome 
        2. for loop --> str
        3. add only elements that are alphanumeric into palimdrome
        4. compare the palindrome with the reverese palidrome: T/F

    I:
    '''
    def isPalindrome(self, s: str) -> bool:
        palindrome = []

        for chr in s:
            if chr.isalnum():
                palindrome.append(chr.lower())
     
        return palindrome == palindrome[::-1]
        
        