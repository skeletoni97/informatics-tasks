def calculate_room_parameters(length, width, height):
    floor_area = length * width
    wall_area = 2 * (length + width) * height
    volume = length * width * height
    paint_cost = wall_area * 125

    return (
        f"Площадь пола: {floor_area:.2f} м²\n"
        f"Площадь стен: {wall_area:.2f} м²\n"
        f"Объём: {volume:.2f} м³\n"
        f"Стоимость покраски: {paint_cost:.2f} руб."
    )


length = float(input("Введите длину: "))
width = float(input("Введите ширину: "))
height = float(input("Введите высоту: "))

print(calculate_room_parameters(length, width, height))