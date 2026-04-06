def convert_temperature(celsius):
    fahrenheit = celsius * 9 / 5 + 32

    if celsius <= 0:
        state = "лёд"
    elif celsius < 100:
        state = "жидкость"
    else:
        state = "пар"
    return (
        f"Температура в Фаренгейтах: {fahrenheit:.2f} °F\n"
        f"Состояние воды: {state}"
    )

celsius = float(input("Введите температуру в °C: "))
print(convert_temperature(celsius))