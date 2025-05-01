def calculate_optimal_alloy():
    try:
        # Ввод количества слитков
        ingots = int(input("Введите количество слитков (144 mB/шт): "))
        total_mass = 144 * ingots

        # Вариант 1: Максимальная медь (65%), минимальные висмут (10%) и цинк (25%)
        copper_max = total_mass * 0.65
        bismuth_min = total_mass * 0.10
        zinc_mid = total_mass * 0.25

        # Вариант 2: Минимальная медь (50%), максимальные висмут (20%) и цинк (30%)
        copper_min = total_mass * 0.50
        bismuth_max = total_mass * 0.20
        zinc_max = total_mass * 0.30

        # Вариант 3: Средние значения (медь 57.5%, висмут 15%, цинк 27.5%)
        copper_avg = total_mass * 0.575
        bismuth_avg = total_mass * 0.15
        zinc_avg = total_mass * 0.275

        # Вывод результатов
        print(f"\nРекомендации для {ingots} слитков ({total_mass} mB):")
        print("----------------------------------------------")
        print("1. Максимальная медь (65%) + минимальный висмут (10%):")
        print(f"   Медь: {copper_max:.2f} mB")
        print(f"   Висмут: {bismuth_min:.2f} mB")
        print(f"   Цинк: {zinc_mid:.2f} mB\n")

        print("2. Минимальная медь (50%) + максимальный висмут (20%):")
        print(f"   Медь: {copper_min:.2f} mB")
        print(f"   Висмут: {bismuth_max:.2f} mB")
        print(f"   Цинк: {zinc_max:.2f} mB\n")

        print("3. Средние значения (медь 57.5%, висмут 15%):")
        print(f"   Медь: {copper_avg:.2f} mB")
        print(f"   Висмут: {bismuth_avg:.2f} mB")
        print(f"   Цинк: {zinc_avg:.2f} mB")

    except ValueError:
        print("Ошибка: введите целое число слитков.")

# Запуск
calculate_optimal_alloy()