class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0 # size를 구현하기 위한 개수 정보 변수

    # push
    # 1) 새로운 노드 new_node
    # head와 tail이 해당 노드를 가리킨다.
    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            # 다른 방법
            # current = self.tail
            # current.next = new_node
            # self.tail = new_node
            
            current = new_node
            self.tail.next = current
            self.tail = current
        self.cnt += 1

    def empty(self):
        is_empty = 0
        if self.head is None:
            is_empty = 1
        return is_empty

    def pop(self):
        if self.empty() == 1:
            self.tail = None
            self.cnt = 0
            return -1
            
        current = self.head
        self.head = self.head.next   
        self.cnt -= 1
        return current.data

    def size(self):
        # 큐에 들어있는 정수 갯수 출력
        # if self.empty() == 1:
        #     return 0

        # length = 0
        # current = self.head
        # while current:
        #     current = current.next
        #     length += 1

        # return length
        
        return self.cnt

    def front(self):
        if self.empty() == 1:
            return -1

        return self.head.data
        
    def back(self):
        if self.empty() == 1:
            return -1

        return self.tail.data

deck = Queue()

N = int(input())

for i in range(1, N + 1):
    deck.push(i)

while(deck.size() != 1):
    deck.pop()
    deck.push(deck.head.data)
    deck.pop()

print(deck.head.data)