"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
"""
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result  = [str(i + 1) for i in range(n)]
        
        f, b, fb = "Fizz", "Buzz", "FizzBuzz"
        for i in range(2, n, 3):
            result[i] = f
        for i in range(4, n, 5):
            result[i] = b
        for i in range(14, n, 15):
            result[i] = fb
        #for i in range(1, n + 1):
#
            #if i % 15 == 0: 
                #result.append("FizzBuzz")
            #
            #if i % 3 == 0: buf = "Fizz"
            #elif i % 5 == 0: buf = "Buzz"
            #else: buf = str(i) 
            #
            #result.append(buf)        
        #
        return result
        

if __name__ == "__main__":
    x = Solution()
    n = 20
    print(x.fizzBuzz(n=n))
