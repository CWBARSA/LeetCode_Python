#给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #单字符本身就是自己的最大回文子串噢        
        if len(s) < 2:
            return s
        #定义待返回的字符串
        self.res = ""
        for i in range(len(s)):
            #这里就是考虑到两种情况，从相同字符拓宽和从相邻字符拓宽
            self.helper(s, i, i)
            self.helper(s, i, i+1)
        return self.res
    
    #分割出来的相同操作函数！ 
    def helper(self,s, left, right):
        #这里是判断当前回文子串两端相同的时候，向两端拓展
        while left>=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            #这里的right-left-1是当前的回文子串长度，大于历史最大值，就更新最大值
        if right -left -1 > len(self.res):
            self.res = s[left+1:right]

def main():
  s1=Solution()
  str1='fefrfed'
  result=s1.longestPalindrome(str1)
  print(result)
  

if __name__=="__main__":main()
  
