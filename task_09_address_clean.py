addresses = [
 " г. Москва, ул. Ленина, д. 10 ",
 "г.Казань,ул.Баумана,д.15",
 " г. Санкт-Петербург, ул. Невский, д. 100 "
]

print("=== СРАВНЕНИЕ ===")

for i, address in enumerate(addresses, start=1):
    cleaned = address.strip()
    cleaned = cleaned.replace("г.", "г. ")
    cleaned = cleaned.replace("ул.", "ул. ")
    cleaned = cleaned.replace("д.", "д. ")
    cleaned = cleaned.replace(",", ", ")
    cleaned = " ".join(cleaned.split())

    print(f"#{i}")
    print(f"ДО: '{address}'")
    print(f"ПОСЛЕ: '{cleaned}'")