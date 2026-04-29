class Solution(object):
    def isPalindrome(self, s):
        a="".join(i for i in s if i.isalnum())
        b=a.lower()
        if(b==b[::-1]):
            return True
        else:
            return False

        
