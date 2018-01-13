class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CLL:          #CLL---> Circular Linked List
    def __init__(self):
        self.last=None
        
    def add_data(self,data):
        temp=Node(data)

        if self.last==None:
            self.last=temp
            self.last.next=self.last
        else:
            temp.next=self.last.next
            self.last.next=temp
            self.last=temp

    def get_data_from(self,index,tot_no,my_list):   #returns data from index to tot_no in my_list
        if index==1:
            self.curr=self.last.next        # curr now points to first element in CLL
        else:
            self.count=1
            self.curr=self.last.next
            while self.count<index:
                self.curr=self.curr.next
                self.count+=1
                
        self.count=tot_no
        while self.count>0:
            my_list.append(self.curr.data)      # getting data into my_list from CLL from "index" to "tot_no"
            self.curr=self.curr.next
            self.count-=1
            
    def print_data(self):
        self.curr=self.last
        self.curr=self.curr.next
        
        while self.curr!=self.last:
            print self.curr.data
            self.curr=self.curr.next
        print self.curr.data
'''        

data=[]        
MyList=CLL()
MyList.add_data(10)
MyList.add_data(20)
MyList.add_data(5)
MyList.add_data(42)

MyList.print_data()

MyList.get_data_from(1,4,data)

for i in data:
    print i
        
'''
