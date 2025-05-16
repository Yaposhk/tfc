def calculate_optimal_alloy():
    try:
        # Ввод общего количества слитков
        ingots = int(input("Введите общее количество слитков: "))

        # Идеальные пропорции для красной стали
        gray_percentage_min, gray_percentage_max = 0.20, 0.25
        yellow_percentage_min, yellow_percentage_max = 0.10, 0.15
        pink_percentage_min, pink_percentage_max = 0.10, 0.15
        black_percentage_min, black_percentage_max = 0.50, 0.55

        # Расчет слитков
        gray_count = round(ingots * gray_percentage_max)
        black_count = round(ingots * black_percentage_max)
        remaining = ingots - (gray_count + black_count)

        # Делим оставшиеся слитки между желтым и розовым
        yellow_count = max(int(remaining / 2), int(ingots * yellow_percentage_min))
        pink_count = ingots - (gray_count + black_count + yellow_count)

        # Проверка на нулевые значения
        if gray_count == 0 or yellow_count == 0 or pink_count == 0 or black_count == 0:
            print("Ошибка: сплав не выйдет, количество слитков одного из типов равно 0.")
            return

        # Расчет массы сплава
        gray_mb = gray_count * 144
        yellow_mb = yellow_count * 144
        pink_mb = pink_count * 144
        black_mb = black_count * 144
        total_mb = gray_mb + yellow_mb + pink_mb + black_mb

        # Процентное содержание
        gray_percent = (gray_mb / total_mb) * 100
        yellow_percent = (yellow_mb / total_mb) * 100
        pink_percent = (pink_mb / total_mb) * 100
        black_percent = (black_mb / total_mb) * 100

        # Вывод результатов
        print(f"\nИдеальные пропорции для красной стали:")
        print(f"Сталь: {gray_count} слитков - {gray_mb} mB ({gray_percent:.1f}%)")
        print(f"Латунь: {yellow_count} слитков - {yellow_mb} mB ({yellow_percent:.1f}%)")
        print(f"Розовое золото: {pink_count} слитков - {pink_mb} mB ({pink_percent:.1f}%)")
        print(f"Чёрная сталь: {black_count} слитков - {black_mb} mB ({black_percent:.1f}%)")
        print(f"\nОбщий объем красной стали: {total_mb} mB (слитков: {ingots})")

    except ValueError:
        print("Ошибка: введите целое число слитков.")

# Запуск
calculate_optimal_alloy()
