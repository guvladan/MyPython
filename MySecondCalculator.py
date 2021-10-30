DaysOfWeek = ["Пн", "Вт", "Ср", "Чт", "Пт"]

playtime = int (input("Сколько времени у тебя в начала недели? "))
MIN_TIME = 1
MAX_TIME = 60

for day in DaysOfWeek:
    result = input(day + " - Дневник прислал вовремя? (y/n)") #создаём присвоения значения
    if result == "y":
        playtime = min(playtime + 10, MAX_TIME)
    elif result == "n":
        playtime = max(playtime - 10, MIN_TIME)

    print(playtime)
