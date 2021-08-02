"""Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        #if x < 0:
            #return False
        #str_x = str(x)
        #for i in range(len(str_x)//2):
            #print(i, len(str_x)-i)
            #if str_x[i] == str_x[len(str_x)-i - 1]:
                #continue
            #else:
                #return False
        #
        #return True
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    x = Solution()
    value = 121
    
    print(x.isPalindrome(value))