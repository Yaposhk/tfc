def calculate_optimal_alloy():
    try:
        # Ввод общего количества слитков
        ingots = int(input("Введите общее количество слитков: "))

        # Идеальные пропорции (69.2%, 15.4%, 15.4%)
        gray_count = round(ingots * 0.692)
        yellow_count = round(ingots * 0.154)
        purple_count = ingots - (gray_count + yellow_count)

        # Проверка корректности распределения и отсутствия нулевых слитков
        if gray_count == 0 or yellow_count == 0 or purple_count == 0:
            print("Ошибка: сплав не выйдет, количество слитков одного из типов равно 0.")
            return

        
        # Расчет массы сплава
        gray_mb = gray_count * 144
        yellow_mb = yellow_count * 144
        purple_mb = purple_count * 144
        total_mb = gray_mb + yellow_mb + purple_mb

        # Процентное содержание
        gray_percent = (gray_mb / total_mb) * 100
        yellow_percent = (yellow_mb / total_mb) * 100
        purple_percent = (purple_mb / total_mb) * 100

        # Вывод результатов
        print(f"\nИдеальные пропорции для черной стали:")
        print(f"Сталь: {gray_count} слитков - {gray_mb} mB ({gray_percent:.1f}%)")
        print(f"Никель: {yellow_count} слитков - {yellow_mb} mB ({yellow_percent:.1f}%)")
        print(f"Черная бронза: {purple_count} слитков - {purple_mb} mB ({purple_percent:.1f}%)")
        print(f"\nОбщий объем черной стали: {total_mb} mB (слитков: {ingots})")

    except ValueError:
        print("Ошибка: введите целое число слитков.")

# Запуск
calculate_optimal_alloy()
