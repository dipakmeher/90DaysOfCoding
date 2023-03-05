class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    def foundCycle(self,head):  
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False # Since fast is moving 2 steps in each iteration, it will reach NULL faster

if __name__=="__main__":
    list1 = LinkedList()

    list1.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(-4)


    list1.head.next = second
    second.next = third
    third.next = fourth
    fourth.next=second

    # temp = list1.head
    # while(temp):
    #     print(temp.data)
    #     temp = temp.next

    print(list1.foundCycle(list1.head))
