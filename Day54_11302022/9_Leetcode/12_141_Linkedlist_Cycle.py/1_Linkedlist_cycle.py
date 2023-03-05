class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    def foundCycle(self,head):  
        if not head or not head.next:
            return False
        hashMap = dict() 
        temp = head
        while(temp):
            if temp in hashMap:
                return True
            hashMap[temp] = temp
            temp = temp.next
        return False

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
