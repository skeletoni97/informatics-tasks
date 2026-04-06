beer_1 = {"Жигулевское", "Guinness", "Heineken", "Corona", "Bud"}
beer_2 = {"Corona", "Bud", "Hoegaarden", "Guinness", "Leffe"}
beer_3 = {"Guinness", "Bud", "Leffe", "Stella Artois", "Corona"}

print(
    f"Все уникальные сорта: {beer_1 | beer_2 | beer_3}\n"
    f"Общие для всех: {beer_1 & beer_2 & beer_3}\n"
    f"Только у первого: {beer_1 - beer_2 - beer_3}\n"
    f"Ровно у двух: {((beer_1 & beer_2) | (beer_1 & beer_3) | (beer_2 & beer_3)) - (beer_1 & beer_2 & beer_3)}"
)