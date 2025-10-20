class Patient:

    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.data[index].urgency < self.data[parent_index].urgency:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right
        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(smallest)

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        root = self.data[0]
        self.data[0] = self.data.pop()  # move last element to root
        self.heapify_down(0)
        return root

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f" - {patient.name} ({patient.urgency})")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]




# Test your MinHeap class here including edge cases
heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.print_heap()

# Peek Test
next_up = heap.peek()
print(f"Next Up: {next_up.name}, {next_up.urgency}")

# Extract Min Test
served = heap.remove_min()
print(served.name) # Taylor
heap.print_heap()

"""
Why is a tree appropriate for the doctor structure?
A tree is best for hierarchical data, allowing efficient organization and retrieval of doctors based on relationships. This means that it can best show who reports to whom, just like a hospital's organizational chart, making it more intuitive and self-explanatory. In this case, Dr. Croft is the top of the hierarchy, with other doctors branching out below, showing they report to Dr. Croft. This is better than other structures specifically because it shows relationships clearly.

When might a software engineer use preorder, inorder, or postorder traversals?
A software engineer might use preorder traversal when they need to create a copy of the tree or serialize it, as it looks at the root before any of the children.
Inorder traversal is useful when the tree is sorted, such as a Binary Search Tree, because it retrieves data in a sorted order.
Postorder traversal is used to delete nodes or free memory, as it looks at the children before the root, ensuring all child nodes are checked before the parent.

How do heaps help simulate real-time systems like emergency intake?
Heaps simulate real-time systems by being a priority queue, always sorted by the most urgent cases, giving immediate access to the patient with the highest priority. This is more efficient and practical than lists or dictionaries, which have to resort themselves everytime a new patient comes in, or one is removed. Heaps are optimized for quick insertions and deletions while maintaining order, ideal for urgency, just like this one.
"""