# Vector class that contains 2D value: x and y
import csv


class Vector2D:
    x: int = 0
    y: int = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    def __str__(self):
        return 'Vector2D (' + str(self.x) + ', ' + str(self.y) + ')'


task_string = "R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, " \
              "R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, " \
              "R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L40, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, " \
              "R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, " \
              "R2, R5, R5, L5, L5, R25, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, " \
              "R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, " \
              "L5, L1, L1, L5, L4, L1, L1, R1 "

# List of orientations. 0 = N, 1 = E, 2 = S, 3 = W
orientations = [0, 1, 2, 3]

# List of orientation names.
orientation_strings = ["north", "east", "west", "south"]

# Store position
position = Vector2D(0, 0)

# Initiate orientation at N, 0
orientation = 0

# Record list of coordinates for visual processing later
coordinates = []

# Vector multipliers to apply to Vector2D dependent on orientation
vector_multipliers = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def update_orientation(direction: str):
    global orientation
    if direction == "R":
        orientation = (orientation + 1) % 4
    else:
        orientation = (orientation - 1) % 4


def orientation_str(input_orientation):
    return orientation_strings[input_orientation]


def move(input_string: str):
    old_position = Vector2D(position.x, position.y)
    turn = input_string[0]
    distance = int(input_string[1:])
    update_orientation(turn)
    position.x += distance * vector_multipliers[orientation][0]
    position.y += distance * vector_multipliers[orientation][1]
    coordinates.append((position.x, position.y))
    print(f'{old_position} facing {orientation_str(orientation)} + {input_string} = {position}')


def measure_distance():
    distance = abs(position.x) + abs(position.y)
    print(f'Total distance = {distance}')


def write_csv():
    with open('output.csv', 'w') as file:
        csv_out = csv.writer(file)
        # csv_out.writerow(['x', 'y'])
        csv_out.writerow([0, 0])
        csv_out.writerows(coordinates)


for event in task_string.split(', '):
    move(event)

measure_distance()

write_csv()
