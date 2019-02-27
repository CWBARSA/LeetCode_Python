#1-两数之和
import time
class TwoSum:
    def __init__(self, data=0):
        self.data = data

    def testsum(self, nums, target):
        self.data = target
        """
        :type nums:List[int]
        :type target:int
        :rtype:List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    result=[i,j]
                    return result
        return result


    def testsum2(self, nums, target):
        self.data = target
        """
        :type nums:List[int]
        :type target:int
        :rtype:List[int]
        """
        result = []
        for i in range(len(nums)):
            num1=nums[i]
            num2=target-num1
            if num2 in nums:
                j=nums.index(num2)
                if i!=j:
                    result=[i,j]
                    return result
        return result

    def testsum3(self, nums, target):
        self.data = target
        """
        :type nums:List[int]
        :type target:int
        :rtype:List[int]
        """
        # 创建字典一，存储输入列表的元素值和对应索引
        num_dict={nums[i]:i for i in range(len(nums))}
        #print(num_dict)
        # 创建另一个字典，存储target-列表中元素的值num_r
        num_dict2={i:target-nums[i] for i in range(len(nums))}
        #print(num_dict2)
        # 判断num_r是否是输入列表中的元素，如果是则返回索引值
        result = []
        for i in range(len(nums)):
            j=num_dict.get(num_dict2.get(i))
            if (j is not None) and (j!=i):
                result=[i,j]
        return result

    def testsum4(self, nums, target):
        self.data = target
        """
        :type nums:List[int]
        :type target:int
        :rtype:List[int]
        """
        # 创建字典一，存储输入列表的元素值和对应索引
        num_dict={nums[i]:i for i in range(len(nums))}
        #print(num_dict)
        result = []
        for i in range(len(nums)-1):
            rest=target-nums[i]
            if rest in num_dict and i!=num_dict[rest]:
                result=[i,num_dict[rest]]
                return result
        return result

egg1 = TwoSum()
nums1 = [4, 5, 9, 8]
nums2 = [4, 5, 9, 8]
nums3 = [4, 5, 9, 8]
nums4 = [4, 5, 9, 8]
target1 = 14

# 计时
start1=time.clock()
result1 = egg1.testsum(nums1, target1)
end1=time.clock()
print('testsum1:Running time: %s Seconds'%(end1-start1))

# 计时
start2=time.clock()
result2 = egg1.testsum2(nums2, target1)
end2=time.clock()
print('testsum2:Running time: %s Seconds'%(end2-start2))

# 计时
start3=time.clock()
result3 = egg1.testsum3(nums3, target1)
end3=time.clock()
print('testsum3:Running time: %s Seconds'%(end3-start3))

# 计时
start4=time.clock()
result4 = egg1.testsum4(nums4, target1)
end4=time.clock()
print('testsum4:Running time: %s Seconds'%(end4-start4))
print(result1)
print(result2)
print(result3)
print(result4)

