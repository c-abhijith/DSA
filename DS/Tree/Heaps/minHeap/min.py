class MaxHeap:
    def __init__(self):
        self.heap = []

    # Function to get the index of the parent of a node
    def parent(self, i):
        return (i - 1) // 2

    # Function to get the index of the left child of a node
    def left_child(self, i):
        return 2 * i + 1

    # Function to get the index of the right child of a node
    def right_child(self, i):
        return 2 * i + 2

    # Insert a new key into the heap
    def insert(self, key):
        self.heap.append(key)  # Insert at the end
        self.heapify_up(len(self.heap) - 1)  # Move the new element up to maintain heap property

    # Heapify up (for insertion)
    def heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(i, self.parent(i))  # Swap if parent is smaller
            i = self.parent(i)

    # Extract the maximum element (root)
    def extract_max(self):
        if len(self.heap) == 0:
            return None

        # The root element is the maximum
        root = self.heap[0]

        # Move the last element to root and remove the last element
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.heapify_down(0)  # Restore heap property
        else:
            self.heap.pop()

        return root

    # Heapify down (for deletion or extraction)
    def heapify_down(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self.heapify_down(largest)

    # Get the maximum element (root) without removing it
    def get_max(self):
        return self.heap[0] if len(self.heap) > 0 else None

    # Swap elements at two indices
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Print the heap
    def print_heap(self):
        print("Heap:", self.heap)


# Min-Heap Example
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(5)
min_heap.print_heap()   # Output: Heap: [5, 20, 10]
print(min_heap.get_min())  # Output: 5
print(min_heap.extract_min())  # Output: 5
min_heap.print_heap()   # Output: Heap: [10, 20]

# Max-Heap Example
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(5)
max_heap.print_heap()  # Output: Heap: [20, 10, 5]
print(max_heap.get_max())  # Output: 20
print(max_heap.extract_max())  # Output: 20
max_heap.print_heap()   # Output: Heap: [10, 5]
