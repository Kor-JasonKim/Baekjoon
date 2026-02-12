class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.top = new_node
        else:
            current = new_node
            current.next = self.top
            self.top = current

    def display(self):
        if self.is_empty():
            return

        current = self.top

        while current:
            print(f"|  {current.data}  |")
            current = current.next

        print("--------")

    def peek(self):
        # top node data 반환
        if self.is_empty():
            return None
        return self.top.data
        
    def pop(self):
        # top node data 반환, top 노드 제거
        if self.is_empty():
            return None

        # 1)
        #current = self.top
        #self.top = self.top.next
        #return current.data

        # 2)
        temp = self.top.data
        self.top = self.top.next
        return temp

def is_check(test):
    vps = Stack()
    
    # YES, NO를 반환 ->
    is_valid = True # 괄호 매칭 완료 -> True, 매칭 실패 -> False
    
    for ps in test:
        if ps == "(":
            vps.push(ps)
        else:
            if vps.pop() == "(":
                continue # 반복문의 다음 회차 진행
            else:
                is_valid = False
                break
    
    if not vps.is_empty():
        is_valid = False
    
    if is_valid:
        print("YES")
    else:
        print("NO")

T = int(input())

for i in range(T):
    test = input()
    is_check(test)