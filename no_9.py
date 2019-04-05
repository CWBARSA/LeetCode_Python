#判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        str_x_re = list(str_x)[::-1]
        str_x_re = "".join(str_x_re)
        return str_x == str_x_re

def main():
  x=212
  solution=Solution()
  result1=solution.isPalindrome(x)
  print(result1)



if __name__=="__main__":main()
