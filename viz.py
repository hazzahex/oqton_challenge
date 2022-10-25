import csv

from PIL import Image, ImageDraw

x_range = [0, 0]
y_range = [0, 0]

x_list = []
y_list = []

coordinates = []


def parse_coordinates():
    global coordinates, x_list, y_list
    with open('output.csv', 'r') as file:
        coordinates = [list(map(int, rec)) for rec in csv.reader(file, delimiter=',')]
        x_list, y_list = list(map(list, zip(*coordinates)))


parse_coordinates()


def update_ranges():
    global x_range, x_list, y_range, y_list
    x_range = [min(x_list), max(x_list)]
    y_range = [min(y_list), max(y_list)]
    print(x_range)
    print(y_range)


update_ranges()


def draw_paths():
    image = Image.new('RGB', (x_range[1] - x_range[0], y_range[1] - y_range[0]))
    draw = ImageDraw.Draw(image)
    draw.line([(-x_range[0], 0), (-x_range[0], y_range[1] - y_range[0])], (255, 0, 0), 1)
    draw.line([(0, -y_range[0]), (x_range[1] - x_range[0], -y_range[0])], (255, 0, 0), 1)
    for i in range(len(x_list) - 1):
        draw.line([(x_list[i] - x_range[0], y_list[i] - y_range[0]), (x_list[i + 1] - x_range[0], y_list[i + 1] - y_range[0])], (i + 10, i + 10, 255), 1)
    image_large = image.resize(((x_range[1] - x_range[0]) * 3, (y_range[1] - y_range[0]) * 3))
    image.save('out.png', "PNG")
    image_large.save('out_large.png', "PNG")


draw_paths()
