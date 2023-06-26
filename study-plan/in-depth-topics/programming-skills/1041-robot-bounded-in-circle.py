# editorial
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # if the direction changes once in the instructions,
        # then iterate the instructions for 4 times is enough

        # directions = [north, east, south, west]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # initial position is the center
        x = y = 0
        # facing north
        index = 0

        for i in instructions:
            if i == 'L':
                index = (index + 3) % 4
            elif i == 'R':
                index = (index + 1) % 4
            else:
                x += directions[index][0]
                y += directions[index][1]
            
        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == y == 0) or index != 0

