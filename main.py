PI = 3.14


def circle_area(r: int | float) -> int | float:

    circle = PI * r ** 2
    return circle


def format_description(r: int | float, area: int | float) -> str:
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_info(r: float):
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_info(radius)
