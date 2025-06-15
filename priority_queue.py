import heapq
import time

class Task:
    def __init__(self, task_id, priority, arrival_time=None, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time or time.time()
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority  # Min-heap by priority

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        heapq.heappush(self.heap, task)

    def extract_min(self):
        return heapq.heappop(self.heap) if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0

    def decrease_priority(self, task_id, new_priority):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                self.heap[i].priority = new_priority
                heapq.heapify(self.heap)
                break
