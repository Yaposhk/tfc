def calculate_optimal_alloy():
    try:
        # Ввод общего количества слитков
        ingots = int(input("Введите общее количество слитков: "))

        # Идеальные пропорции для розового золота
        red_percentage_min, red_percentage_max = 0.15, 0.30
        gold_percentage_min, gold_percentage_max = 0.70, 0.85

        # Расчет слитков
        gold_count = round(ingots * gold_percentage_max)
        red_count = ingots - gold_count

        # Проверка на нулевые значения
        if gold_count == 0 or red_count == 0:
            print("Ошибка: сплав не выйдет, количество слитков одного из типов равно 0.")
            return

        # Расчет массы сплава
        gold_mb = gold_count * 144
        red_mb = red_count * 144
        total_mb = gold_mb + red_mb

        # Процентное содержание
        gold_percent = (gold_mb / total_mb) * 100
        red_percent = (red_mb / total_mb) * 100

        # Вывод результатов
        print(f"\nИдеальные пропорции для розового золота:")
        print(f"Медь: {red_count} слитков - {red_mb} mB ({red_percent:.1f}%)")
        print(f"Золото: {gold_count} слитков - {gold_mb} mB ({gold_percent:.1f}%)")
        print(f"\nОбщий объем розового золота: {total_mb} mB (слитков: {ingots})")

    except ValueError:
        print("Ошибка: введите целое число слитков.")

# Запуск
calculate_optimal_alloy()
