class Solution:
    def countCollisions(self, directions: str) -> int:
        collisions = 0
        right = 0
        car_on_left = False
        for i, d in enumerate(directions):
            if d == 'R':
                right += 1
            elif d == 'L':
                if right:
                    collisions += right+1
                    right = 0
                    car_on_left = True
                elif car_on_left:
                    collisions += 1
            else:
                collisions += right
                right = 0
                car_on_left = True
        return collisions