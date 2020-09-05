import queue

class Stack(object):
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
    def push(self,val):
        self.q1.put(val)
    def pop(self):

        if self.q1.qsize()==0:
            return None
        while 1:
            if self.q1.qsize()==1:
                item = self.q1.get()
                break

            self.q2.put(self.q1.get())
        self.q1,self.q2=self.q2,self.q1

        return item

o  = Stack()
print(o.push(1))
print(o.push(2))
print(o.push(3))



print(o.pop())
print(o.pop())
print(o.pop())

