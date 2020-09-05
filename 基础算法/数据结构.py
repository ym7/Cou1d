'''
一：栈
特性：先进后出的数据结构,具有栈顶和栈尾。
应用：
Stack() 创建一个空的新栈。 它不需要参数，并返回一个空栈。
push(item)将一个新项添加到栈的顶部。它需要 item 做参数并不返回任何内容。
pop() 从栈中删除顶部项。它不需要参数并返回 item 。栈被修改。
peek() 从栈返回顶部项，但不会删除它。不需要参数。 不修改栈。
isEmpty() 测试栈是否为空。不需要参数，并返回布尔值。
size() 返回栈中的 item 数量。不需要参数，并返回一个整数。
'''


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return len(self.items) - 1

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

# items = [1,2,3] 1通过append先进。3通过pop先出。

print('栈顶元素下标：', stack.peek())
print(stack.isEmpty())
print('元素个数：', stack.size())
print(stack.pop())
print(stack.pop())
print(stack.pop())

# 打印结果
# 栈顶元素下标： 2
# False
# 元素个数： 3
# 3
# 2
# 1


'''
二：队列
队列：先进先出
Queue() 创建一个空的新队列。 它不需要参数，并返回一个空队列。
enqueue(item) 将新项添加到队尾。 它需要 item 作为参数，并不返回任何内容。
dequeue() 从队首移除项。它不需要参数并返回 item。 队列被修改。
isEmpty() 查看队列是否为空。它不需要参数，并返回布尔值。
size() 返回队列中的项数。它不需要参数，并返回一个整数。
'''


class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

# items = [3,2,1] 1先insert（0）先进，1通过pop先出

# 1
# 2
# 3


'''
案列：
6个孩子围城一个圈，排列顺序孩子们自己指定。
第一个孩子手里有一个烫手的山芋，需要在计时器计时1秒后将山芋传递给下一个孩子，依次类推。
规则是，在计时器每计时7秒时，手里有山芋的孩子退出游戏。该游戏直到剩下一个孩子时结束，最后剩下的孩子获胜。
请使用队列实现该游戏策略，排在第几个位置最终会获胜。

准则：手里有山芋的孩子永远排在队列的头部
'''

kids = ['A', 'B', 'C', 'D', 'E', 'F']
# 创建一个队列
queue = Queue()

for kid in kids:
    a = queue.enqueue(kid)
while queue.size() > 1:
    for i in range(6):
        kid = queue.dequeue()
        queue.enqueue(kid)
    queue.dequeue()

print('winner is ', queue.dequeue())
# winner is E


'''
三：双端队列
同同列相比，有两个头部和尾部。
可以在双端进行数据的插入和删除，
提供了单数据结构中栈和队列的特性
应用：
Deque() 创建一个空的新 deque。它不需要参数，并返回空的 deque。
addFront(item) 将一个新项添加到 deque 的首部。它需要 item 参数 并不返回任何内容。
addRear(item) 将一个新项添加到 deque 的尾部。它需要 item 参数并不返回任何内容。
removeFront() 从 deque 中删除首项。它不需要参数并返回 item。deque 被修改。
removeRear() 从 deque 中删除尾项。它不需要参数并返回 item。deque 被修改。
isEmpty() 测试 deque 是否为空。它不需要参数，并返回布尔值。
size() 返回 deque 中的项数。它不需要参数，并返回一个整数。
'''


class Deque():
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addBehind(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def removeBehind(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


q = Deque()
q.addFront(1)
q.addFront(2)
q.addFront(3)

print(q.removeBehind())
print(q.removeBehind())
print(q.removeBehind())

# 3
# 2
# 1

'''
双端队列应用案例：
回文检查
回文是一个字符串，读取首尾相同的字符，例如，radar toot madam。
'''


def doit(string):
    ex = {
        '1': '是回文',
        '2': '不是回文'
    }
    twoq = Deque()
    for ch in string:
        twoq.addFront(ch)
    while twoq.size() > 1:
        if twoq.removeFront() != twoq.removeBehind():
            return ex['2']
    return ex['1']


print(doit('wahthaw'))

'''
四：内存
计算机的作用↓↓
用来存储和运算二进制的数据
问题：计算机如何计算1+2？
    - 将1和2的二进制类型的数据加载到计算机的内存中，
      然后使用寄存器进行数值的预算。
变量的概念
    变量就是某一块内存
    内存空间是有两个默认的属性：
        内存空间的大小
            bit（位）：一个bit大小的内存空间只能存放一位二进制的数
            byte（字节）：8bit
            kb：1024byte
        内存空间的地址
            使用一个十六进制的数值表示
            作用：让cup寻址
理解a=10的内存图（引用，指向）
    引用：
        变量==》内存空间的地址
        a = 10：a变量/引用/内存空间的地址
    指向：
        如果变量或者引用表示的是某一块内存空间地址的话，
        则该变量或者该引用指向了该块内存                    
'''

'''
五：顺序表↓↓
集合中存储的元素是有顺序的，
顺序表的结构可以分为两种形式：
    单数据类型和多数据类型。
python中的列表和元组就属于多数据类型的顺序表
多数据类型顺序表的内存图（内存非连续开辟）
顺序表的弊端：
    顺序表的结构需要预先知道数据大小来申请连续的存储空间，而在进行扩充时又需要进行数据的搬迁。    
'''

'''
六：链表↓↓
链表：
    相对于顺序表，链表结构可以充分利用计算机内存空间，实现灵活的内存动态管理且进行扩充时不需要进行数据搬迁。
    【data|next】------【data2|next】------【data3|next】
    data为自定义的数据，next为下一个节点的地址。
链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是不像顺序表一样连续存储数据，而是每一个结点（数据存储单元）里存放下一个结点的信息（即地址）
.is_empty()：链表是否为空
. length()：链表长度
. travel()：遍历整个链表
. add(item)：链表头部添加元素
. append(item)：链表尾部添加元素
. insert(pos, item)：指定位置添加元素
. remove(item)：删除节点
. search(item)：查找节点是否存在
'''


class Node(object):
    def __init__(self, data):
        # data: 节点保存的数据
        # next: 保存下一个节点对象
        self.data = data
        self.next = None


class Link(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    # 向链表头部插入一个节点
    def add(self, data):
        """将新节点添加到链表头部。
        即头指针指向新节点，尾节点的指针指向新节点，
        新节点的指针指向原头节点"""
        node = Node(data)
        # 指向的是节点，不是数据
        node.next = self._head
        self._head = node

    def travel(self):
        '''
        遍历列表
        :return:
        '''
        # _head在链表创建好之后一定是不可变,所以要给他赋值为新节点
        cur = self._head
        ls = []
        while cur:
            print(cur.item)
            cur = cur.next

    def size(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def append(self, item):
        """与add方法唯一的区别为链表头的指针不变"""
        node = Node(item)
        if self._head == None:
            self._head = node
            return
        cur = self._head
        pre = None  # 指向cur前一个节点
        while cur:
            pre = cur
            cur = cur.next
        pre.next = node

    def search(self, item):
        find = False

        cur = self._head
        while cur:
            if cur.item == item:
                find = True
                break
            cur = cur.next

        return find

    def insert(self, pos, item):
        node = Node(item)
        pre = None  # 指向cur前一个节点
        cur = self._head
        for i in range(pos):
            pre = cur
            cur = cur.next
        pre.next = node
        node.next = cur

    def remove(self, item):
        cur = self._head
        pre = None  # 指向cur前一个节点
        # 删除的是第一个节点
        if cur.item == None:
            self._head = cur.next
            return
        while cur:
            pre = cur
            cur = cur.next
            if cur.next == None:
                return
            if cur.item == item:
                pre.next = cur.next
                return


link = Link()

link.append(1)
link.append(2)
link.append(3)
link.append(4)
# link.insert(2,1.3)
# link.remove(5)
link.travel()

# 1
# 2
# 3
# 4


'''
七：二叉树 ↓↓
二叉树的遍历：
广度优先遍历--》一层一层对节点进行遍历
深度优先遍历--》前序：根左右
            中序：左根右
            后序：左右根
特性：由其树状结构，对其做删除与插入是扰乱其结构的。所以之只能进行添加与查询。
作用：数据库、文件系统结构
时间复杂度：O(n)
'''


class Node(object):
    '''创建节点'''

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree(object):
    '''创造一颗树'''

    def __init__(self):
        self.root = None

    def addNode(self, item):
        node = Node(item)
        '''如果书的根节点root是空，那么就创建第一个根节点root=node'''
        if self.root == None:
            self.root = node
            return
        cur = self.root  # 根节点root创建了只有一个，所以赋值给cur
        q = [cur]  # 列表元素是遍历判断的节点

        while q:
            new_node = q.pop(0)
            if new_node.left == None:
                new_node.left = node
                return
            else:
                q.append(new_node.left)
            if new_node.right == None:
                new_node.right = node
                return
            else:
                q.append(new_node.right)

    def travel(self):
        cur = self.root
        q = [cur]
        while q:
            nd = q.pop(0)
            print(nd.item)
            if nd.left:
                q.append(nd.left)
            elif nd.right:
                q.append(nd.right)

    '''深度优先遍历'''
    def front(self,root): #前序：根左右
        if root == None:
            return
        print(root.item)
        self.front(root.left)
        self.front(root.right)

    def mid(self,root):#中序：左根右
        if root == None:
            return
        self.mid(root.left)
        print(root.item)
        self.mid(root.right)

    def back(self,root):
        if root == None:#后序：左右根
            return
        self.back(root.left)
        self.back(root.right)
        print(root.item)



'''
排序二叉树
乱序数据的插入的时候，需要遵从一个准则：
    插入的第一个数值作为树的根节点
    后序插入的数值，如果比根节点小，插入根节点的左侧，否则插入到根节点的右侧
'''
class Node():
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

class SortTree():
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        cur = self.root
        if self.root == None:
            self.root = node
            return
        while cur :
            if item > cur.item:#向右侧插入
                if cur.right == None:
                    cur.right = node
                    break
                else:
                    cur = cur.right #使节点偏移
            else:
                if cur.left == None:
                    cur.left = node
                    break
                else:
                    cur = cur.left

    def mid(self,root):#中序：左根右
        if root == None:
            return
        self.mid(root.left)
        print(root.item)
        self.mid(root.right)