# 다음 API를 지원하는 Linked List 구현
# insert(index, item): index 위치에 item 삽입
# delete(index): index 위치의 원소 삭제
# get(index): index 위치의 원소 반환
# update(index, item): index 위치 값을 item으로 변경
# length(): 리스트 길이 반환
# isEmpty(): 리스트가 비어있는지 확인

# 실행할 때는 New Terminal 열어 실행 (Ctrl+Shift+`)
# 터미널 나갈 때는 exit()

class Node:
    def __init__(self, data):
        self.data = data    # data: 실제 데이터 저장
        self.next = None    # next: 뒤에 따르는 node 저장

class LinkedList:
    def __init__(self):
        self.head = None    # head: Linked List의 첫 시작 Node
    
    def isEmpty(self):
        return self.head is None
    
    def length(self):
        # head 부터 시작해 Null이 아니면 한 칸씩 전진하며 개수 확인
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    # 출력하는 함수
    def print_List(self):
        current = self.head
        while current:
            print(current.data, end= '->')
            current = current.next
        print('None')
    
    # 원하는 위치(index번째)에 새로운 노드를 삽입하는 함수
    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:  # 맨 앞에 새로 삽입한 linked_list의 노드를 새로운 head로 가리키게 함
            new_node.next = self.head
            self.head = new_node
            return
    
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next    # prev의 다음 칸을 한 칸씩 이어나가기
        
        new_node = prev.next    # 삽입한 노드를 원래 n번째 노드의 next로 지정
        prev.next = new_node    # 원래 n+1번째 노드를 삽입한 노드의 next로 지정
        
    def delete(self, index):
        # linked list가 비어있는가?
        if self.head is None:
            raise IndexError("Index out of range")
            # 에러 발생시킴

        # head를 삭제하는지?
        if index == 0:
            self.head = self.head.next
            return
        
        # 그렇지 않을 경우
        prev = self.head
        for _ in range(index - 1):
            if prev is None:
                raise IndexError("Index out of range")
            prev = prev.next

        # 지우려 하는 node의 앞까지 왔으니, 지우려는 해당 node가 존재하는지 확인
        if prev.next is None:
            raise IndexError("Index out of range")
        
        # 지울 node의 앞에 있는 node와 뒤에 있는 node를 이어줌
        prev.next = prev.next.next

# 터미널 실행
# from linked_list import LinkedList
# ll = LinkedList()
# ll
# ll.isEmpty()    # True
# ll.length       # 0
# ll.insert(0, 'A')
# ll.isEmpty()    # False
# ll.insert(1, 'B')
# ll.insert(1, 'C')
# ll.print_List()

    # get: 해당 index 위치의 data 반환 (비어있지 않으면)
    def get(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        
        if current is None:
            raise IndexError("Index out of range")
        
        return current.data

    # update: 해당 index 위치의 data 변경 (비어있지 않으면)
    def update(self, index, data):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        
        if current is None:
            raise IndexError("Index out of range")

        current.data = data