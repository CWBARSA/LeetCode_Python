#给定一个 32 位有符号整数，将整数中的数字进行反转。

class Solution:
    def reverseNum(self, x):
        """
        :type x: int
        :rtype: int
        """
        #先记录正负
        sign = [1,-1][x < 0]
        #利用正负反转后符号不变，并利用绝对值函数进行反转，添加原有符号即可
        rst = sign * int(str(abs(x))[::-1])
        #返回反转值，超出32位为0
        return rst if -(2**31)-1 < rst < 2**31 else 0

def main():
  s=Solution()
  x=123456
  y=-3452
  result1=s.reverseNum(x)
  result2=s.reverseNum(y)
  print(x,":",result1)
  print(y,":",result2)

if __name__=="__main__":main()
