#给定一个字符串，找出不含有重复字符的最长子串的长度。


def subString(s):
        """
        :type s: str
        :rtype: int
        """
        #创建一个空字典，其存放的形式是“单字符:出现位置的索引”
        indexDict = {}
        #存放记录最大长度和当前循环下的长度
        maxLength = currMax = 0
        for i in range(len(s)):
            #这里是当s[i]没有在之前出现过，则当前长度currMax自动加一
            #当出现了重复字符，则比较当前找到的子字符串长度和历史最大长度
            #重点是这里i - indexDict[s[i]] - 1 的含义；代码后举例具体讲解
            if s[i] in indexDict and i - indexDict[s[i]] - 1 <= currMax:
                if maxLength < currMax:
                    maxLength = currMax
                currMax = i - indexDict[s[i]] - 1
            currMax = currMax + 1                
            indexDict[s[i]] = i 
        return maxLength if currMax < maxLength else currMax


if __name__=="__main__":print(subString("wewuddjrr"))
