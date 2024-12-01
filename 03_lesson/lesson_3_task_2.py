from smartphone import Smartphone
catalog = [
    Smartphone("Apple","16 Pro MAX","+7965 543 54 23"),
    Smartphone("Samsung","Galaxy S24 Ultra","+7938 766 86 34"),
    Smartphone("Xiaomi","14","+7996 086 86 01")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.phone_number}")
