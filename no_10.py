#给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
#'.' 匹配任意单个字符。
#'*' 匹配零个或多个前面的元素。

"""

三、re模块中常用功能函数

match()
匹配string 开头，成功返回Match object, 失败返回None，只匹配一个。

search()
在string中进行搜索，成功返回Match object, 失败返回None, 只匹配一个。

findall()
在string中查找所有 匹配成功的组, 即用括号括起来的部分。
返回list对象，每个list item是由每个匹配的所有组组成的list。

finditer()
在string中查找所有 匹配成功的字符串, 返回iterator，每个item是一个Match object。

group()
是将所有匹配符合条件的字符串，打包成一个组，即group。
其中编号为0的group，即group(0)表示匹配的整个字符串。
其他编号分别为1,2,3，…的表示匹配成功返回的组中的每个字符串。

split()
按照能够匹配的子串将string分割后返回列表。
可以使用re.split来分割字符串，如：re.split(r'\s+', text)；将字符串按空格分割成一个单词列表。

"""

import re
class Solution(object):
    def isMatch(self, s, p):
        ans = (re.match(p, s))
        if (ans == None):
            return False
        if (ans.group(0) != s):
            return False
        return True
      
s = Solution()
print(s.isMatch("ab", ".b"))

