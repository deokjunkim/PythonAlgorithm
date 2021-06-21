import heapq

REMOVED = "r"


class DoublePriorityQueue:

    def __init__(self):

        self.entry_finder = {}
        self.min_heap = []
        self.max_heap = []
        self.cnt = 0

    def _check_empty(self, q) -> bool:
        while q and q[0][1] == REMOVED:
            heapq.heappop(q)
        if not q:
            return True
        return False

    def insert(self, v):
        print(self.entry_finder)
        vid = self.cnt
        min_ele, max_ele = [v, vid], [-v, vid]
        heapq.heappush(self.min_heap, min_ele)
        heapq.heappush(self.max_heap, max_ele)
        self.entry_finder[vid] = [min_ele, max_ele]
        self.cnt += 1
        print(self.entry_finder)
        print()

    def pop_min(self):
        is_empty = self._check_empty(self.min_heap)
        if not is_empty:
            print(self.entry_finder)
            value, vid = heapq.heappop(self.min_heap)
            entries = self.entry_finder.pop(vid)
            entries[1][1] = REMOVED
            print(self.entry_finder, self.min_heap)
            print()

    def pop_max(self):
        is_empty = self._check_empty(self.max_heap)
        if not is_empty:
            print(self.entry_finder)
            value, vid = heapq.heappop(self.max_heap)
            entries = self.entry_finder.pop(vid)
            entries[0][1] = REMOVED
            print(self.entry_finder, self.max_heap)
            print()

    def get_min(self):
        if not self._check_empty(self.min_heap):
            return self.min_heap[0][0]
        return 0

    def get_max(self):
        if not self._check_empty(self.max_heap):
            return - self.max_heap[0][0]
        return 0


def solution(operations):
    dpq = DoublePriorityQueue()

    for each in operations:
        op, num = each.split(" ")
        num = int(num)
        if op == "I":
            dpq.insert(num)
        elif op == "D" and num == -1:
            dpq.pop_min()
        else:
            dpq.pop_max()

    return [dpq.get_max(), dpq.get_min()]

solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])