class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Queue is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Queue is empty/")

    def __repr__(self):
        return repr(self.items)

class Deque(Queue):

    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        value = self.items.pop(0)
        if value is not None:
            return value
        else:
            print("Deque is empty. ")

if __name__ == "__main__":
    deque = Deque()
    print("테크(Deque)가 비었나요? {0}".format(deque.isEmpty()))
    print("테크에 숫자 0~9를 추가합니다.")
    for i in range(10):
        deque.enqueue(i)
    print("데크 크기: {0}".format(deque.size()))
    print("peek: {0}".format(deque.peek()))
    print("dequeue: {0}".format(deque.dequeue()))
    print("peek: {0}".format(deque.peek()))
    print("데크가 비었나요? {0}".format(deque.isEmpty()))
    print()
    print("데크: {0}".format(deque))
    print("dequeue: {0}".format(deque.dequeue_front()))
    print("peek: {0}".format(deque.peek()))
    print("데크: {0}".format(deque))
    print("enqueue_back(50)을 수행합니다.")
    deque.enqueue_back(50)
    print("peek: {0}".format(deque.peek()))
    print("데크: {0}".format(deque))
    print()
    from collections import deque
    q = deque(["버퍼","젠더","윌로"])
    print(q)
    q.append("자일스")
    print(q)
    print(q.popleft())
    print(q.pop())
    print(q)
    q.appendleft('엔젤')
    print(q)
    print()
    q.rotate(1)
    print(q)
    q.rotate(2)
    print(q)
    q.rotate(3)
    print(q)
    q.rotate(4)
    print(q)
    q.rotate(-1)
    print(q)
    q.rotate(-2)
    print(q)