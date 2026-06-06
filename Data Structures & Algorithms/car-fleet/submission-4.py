class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #since cars cannot overtake, maintain a stack in terms of their initial positions
        #only start popping when the first car reaches target, then pop all the consecutive following that has reached the target too
        sorted_position = sorted(position)
        output = 0
        time_taken_list = []
        for pos in sorted_position:
            speed_idx = position.index(pos)
            time_taken = (target - position[speed_idx]) / speed[speed_idx]
            time_taken_list.append(time_taken)
        
        while time_taken_list:
            output += 1
            curr = time_taken_list.pop()       
            while time_taken_list and time_taken_list[-1] <= curr:
                print("POPPING", time_taken_list[-1], "FOR FLEET", output)
                time_taken_list.pop()
        return output

                