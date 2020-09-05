class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Link(object):
    def __init__(self):
        self._head = None

    def add(self, data):
        node = Node(data)
        node.next = self._head
        self._head = node

    def travel(self):
        cur = self._head
        while cur:
            print(cur.data)
            cur = cur.next

    def isEmpty(self):
        return self._head==None

    def size(self):
        cur = self._head
        count = 0
        while cur:
            count+=1
            cur = cur.next

        return count

    def append(self,data):
        node = Node(data)
        if self._head == None:
            self._head = node
            return
        else:
            cur = self._head
            pre = None
            while cur:
                pre = cur
                cur = cur.next

            pre.next = node


    def search(self,data):
        find = False
        cur = self._head
        while cur:
            if cur.data == data:
                find = True
                break
            else:
                cur = cur.next
        return find


    def insert(self,position,data):
        node = Node(data)
        pre = None
        cur = self._head
        for i in range(position):
            pre = cur
            cur = cur.next
        pre.next= node
        node.next = cur

    def remove(self,data):
        pass




l = Link()
l.add(2)
l.add(3)

l.travel()

print(l.size())