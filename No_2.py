#两数相加

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val,next=None):
         self.val = val
         self.next = None

class addTwo:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 先初始化temp链表，l3链表指向temp的0值地址
        temp =ListNode(0)
        l3 = temp
        a = 0
        # 当l1不为空或者l2不为空或者a不等于0的时候
        while l1 != None or l2 != None or a != 0:
            if l1 != None:
                # a等于a加上l1当前的值
                a += l1.val
                # l1的指针指向下一个
                l1 = l1.next
            if l2 != None:
                a += l2.val
                l2 = l2.next
                # temp的下一个的值就是 a%10
            temp.next = ListNode(a % 10)
            temp = temp.next
            a = a // 10
        # l3代替temp来输出链表
        return l3.next
