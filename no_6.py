#将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数，之后从左往右，逐行读取字符：
#"PAHNAPLSIIGYIR"实现一个将字符串进行指定行数变换的函数

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_length = len(s)
        node_length = 2*numRows - 2  # 两列之间的差
        #其实并不需要第一种方法那样列表字符串来回折腾。。。
        result = ""
        #极端特殊情况，直接返回原字符串
        if str_length == 0 or numRows == 0 or numRows == 1:
            return s
        # 从第一行遍历到最后一行
        for i in range(numRows): 
            #大的改进在这里！！！不再逐一遍历，而相当于j += node_length
            for j in range(i, str_length, node_length):
                # 第一行和最后一行  还有普通行的整列数字      
                result += s[j]
                print(result,j)
                #不是第一行和最后一行，且不说普通垂直的时，j-*i+node_length得到第i行斜着的那部分需输出的字符
                if i != 0 and i != numRows-1 and j - 2*i + node_length < str_length:
                    result += s[j-2*i+node_length]  # 单列行的数字
        return result

def main():
  solution=Solution()
  str1='PAYPALISHIRING'
  numRows=4
  result=solution.convert(str1,numRows)
  print(str1+"\n"+result)

if __name__=="__main__":main()
  
