import random
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data
        
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next


class Linked_list(object):
    def __init__(self):
        self.head = None
    #增
    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    #查   
    def search(self, data):
        checking = self.head 
        while checking != None :
            if checking.get_data() == data: 
                return True
            checking = checking.get_next() 
        return False 
    #改
    def change(self, data, new_data):
        checking = self.head 
        while checking != None :
            if checking.get_data() == data: 
                break
            checking = checking.get_next() 
        checking.set_data(new_data)
    #删   
    def remove(self, data):
        checking = self.head 
        previous = None 
        
        while checking != None :
            if checking.get_data() == data: 
                break
            previous = checking 
            checking = checking.get_next() 
         
        if previous == None:
            self.head = checking.get_next()
        else: 
            previous.set_next(checking.get_next())
        

    #返回链表长度
    def size(self):
        count = 0
        counting = self.head #从头结点开始计数
        while counting != None :
            count += 1
            counting = counting.get_next()
        return count

mylink=Linked_list()
print("将0~38之间的偶数加入链表")
for i in range(20):
    mylink.add(2*i)
print("查找10",mylink.search(10))
print("查找20",mylink.search(10))
print("查找15",mylink.search(15))
print("删除10")
mylink.remove(10)
print("查找10",mylink.search(10))
print("修改20-->21",mylink.change(20,21))
print("查找21",mylink.search(21))