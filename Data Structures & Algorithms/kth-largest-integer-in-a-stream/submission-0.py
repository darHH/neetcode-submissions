class KthLargest:

    # implement a min heap - root is smallest
    # keep the heap at k elements always. then answer will be the root val.
    # left child of ith element is 2i + 1
    # right child of ith element is 2i + 2
    # parnet of ith element is (i-1)/2
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for number in nums:
            self.add(number)

    def add(self, val: int) -> int:

        # implement a max heap
        # if already have k elements
        if len(self.heap) >= self.k:
            if val > self.heap[0]:
                self.heap[0] = val
                curr_idx = 0
                # heapify down
                # if curr is larger than child
                while curr_idx * 2 + 1 < len(self.heap): 
                    # if there is a right child and if its smaller than the left child, swap with right child
                    if curr_idx * 2 + 2 < len(self.heap) and self.heap[curr_idx * 2 + 2] < self.heap[curr_idx * 2 + 1]:
                        curr_child_idx = curr_idx * 2 + 2
                    # else swap with right
                    else:
                        curr_child_idx = curr_idx * 2 + 1
                    if self.heap[curr_child_idx] < self.heap[curr_idx]:
                        # swap curr with child
                        temp = self.heap[curr_child_idx]
                        self.heap[curr_child_idx] = self.heap[curr_idx]
                        self.heap[curr_idx] = temp
                        curr_idx = curr_child_idx
                    else:
                        break
        else:
            self.heap.append(val)
            curr_idx = len(self.heap) - 1
            # heapify up
            while (curr_idx - 1) // 2 >= 0 and self.heap[(curr_idx - 1) // 2] > self.heap[curr_idx]:
                curr_parent_idx = (curr_idx - 1) // 2
                # swap curr with parent
                temp = self.heap[curr_parent_idx]
                self.heap[curr_parent_idx] = self.heap[curr_idx]
                self.heap[curr_idx] = temp
                curr_idx = curr_parent_idx

        return self.heap[0]
        
