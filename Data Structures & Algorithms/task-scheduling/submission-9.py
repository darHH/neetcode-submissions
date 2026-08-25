import heapq 
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # initial thoughts: collapse the list into tuples with (count, letter)
        # then we maintain a max heap then we pop and decrement or remove from this heap from the biggest count tuple
        # this tuple will stay in a set for n turns until it is allowed to be "used" again
        tasks.sort()
        tasks_w_count = []
        curr_letter = tasks[0]
        curr_count = 0
        for letter in tasks:
            if letter == curr_letter:
                curr_count += 1
            elif letter != curr_letter:
                task_w_count = [-curr_count, curr_letter]
                heapq.heappush(tasks_w_count, task_w_count)
                curr_letter = letter
                curr_count = 1
        task_w_count = [-curr_count, curr_letter]
        heapq.heappush(tasks_w_count, task_w_count)
        # print(tasks_w_count)

        count = 0
        temp_store = deque()
        while len(tasks_w_count) > 0 or len(temp_store) > 0:
            if len(tasks_w_count) == 0:
                count = temp_store[0][1]     
            else:
                count += 1

            while temp_store and temp_store[0][1] <= count:
                heapq.heappush(tasks_w_count, temp_store.popleft()[0])

            if tasks_w_count:
                curr_task = heapq.heappop(tasks_w_count)
                curr_task[0] += 1
                if curr_task[0] < 0:
                    temp_store.append([curr_task, count + n + 1])

                # print("COUNT:", count)
                # print("HEAP:", tasks_w_count)
                # print("TEMP STORE:", temp_store)

        return count