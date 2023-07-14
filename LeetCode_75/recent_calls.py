import copy

class Queue:
    def __init__(self):
        self.queue = []
        self.length = 0

    def add(self, item):
        self.queue.append(item)
        self.length += 1

    def pop(self):
        x = self.peek()
        self.queue.pop(0)
        self.length -= 1
        return self.peek

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return self.length == 0 

    
class RecentCounter:

    def __init__(self):
        self.queue = Queue()

    def ping(self, t: int) -> int:
        self.queue.add(t)
        output = []
        output_queue = copy.deepcopy(self.queue)
        while output_queue.length >= 1 and t>= output_queue.peek() >= t - 3000:
           output.insert(0, output_queue.pop())
        return output 
    


if __name__ == "__main__":
    counter = RecentCounter()
    print(counter.ping(1))
