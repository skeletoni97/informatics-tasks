def get_work_schedule(day_number):
    days = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
    ]
# Немного расширил условие: программа работает не только для чисел от 1 до 7,
# но и для любых номеров дней, используя повторение дней недели по кругу.
    day_index = (day_number - 1) % 7
    day_name = days[day_index]

    if day_index < 5:
        mode = "рабочий день, 8:00 - начало смены"
    else:
        mode = "выходной, Отдых"

    return f"День недели: {day_name}\nРежим: {mode}"


day_number = int(input("Введите номер дня: "))
print(get_work_schedule(day_number))