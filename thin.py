# Vector class that contains 2D value: x and y
class Vector2D:
    x = 0
    y = 0


# String from txt file
task_string = "R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, " \
              "R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, " \
              "R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L40, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, " \
              "R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, " \
              "R2, R5, R5, L5, L5, R25, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, " \
              "R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, " \
              "L5, L1, L1, L5, L4, L1, L1, R1 "


# List of orientations. 0 = N, 1 = E, 2 = S, 3 = W
orientations = [0, 1, 2, 3]

# Store position
pos = Vector2D

# Initiate orientation at N, 0
o = 0

# Vector multipliers to apply to Vector2D dependent on orientation
vec_mult = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# Updated orientation based on turn direction
def turn(r: str):
    global o
    if r == "R":
        o = (o + 1) % 4
    else:
        o = (o - 1) % 4


# Move agent to new position based on command
def move(i: str):
    r = i[0]  # Extract turn direction
    d = int(i[1:])  # Extract int for distance travelled
    turn(r)  # Rotate agent
    pos.x += d * vec_mult[o][0]  # Update x position based on distance and new orientation
    pos.y += d * vec_mult[o][1]  # Update y position based on distance and new orientation


def measure_distance():
    print(f'Total distance = {abs(pos.x) + abs(pos.y)}')


for e in task_string.split(', '):
    move(e)

measure_distance()
