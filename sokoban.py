px = 2
py = 1
bx = 3
by = 3

screen_width = 4
screen_height = 4


def in_map(x, y, screen_width, screen_height):
    if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
        return False
    return True


def move(x, y, dx, dy):
    return [x + dx, y + dy]

while True:
    for y in range(screen_height):
        for x in range(screen_width):
            if x == px and y == py:
                print("T ", end="")
            elif x == bx and y == by:
                print("B ", end="")
            else:
                print("- ", end="")
        print()

    choice = input("What do you want? U - D - L - R: ").upper()

    dx = 0
    dy = 0

    if choice == "W":
        dy = -1
    elif choice == "S":
        dy = 1
    elif choice == "A":
        dx = -1
    elif choice == "D":
        dx = 1

    [next_px, next_py] = move(px, py, dx, dy)

    if not in_map(next_px, next_py, screen_width, screen_height):
        print("Go away!!!")
    else:
        px = next_px
        py = next_py

# https://codeshare.io/29OkY1