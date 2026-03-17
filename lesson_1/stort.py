# Инициализация переменных
total_sum = 0
basket = []

print("=== СИСТЕМА УЧЕТА ПРОДАЖ v1.0 ===")
print("(для завершения введите 'стоп')")

while True:
    item = input("\nТовар: ").strip().lower()
    
    if item == "стоп":
        print("Сбор данных завершен.")
        break
    
    try:
        # Ввод и преобразование типов
        price = float(input(f"Цена за {item}: "))
        quantity = int(input(f"Количество: "))
        
        # Расчеты
        revenue = price * quantity
        total_sum += revenue
        
        # Добавление в корзину (список)
        record = f"{item.capitalize()}: {quantity} шт. x {price} руб. = {revenue} руб."
        basket.append(record)
        
        print(f"Успешно добавлено. Выручка: {revenue}")
        
        # Условие для крупной сделки
        if revenue > 50000:
            print("⭐ МЕГА-ПРОДАЖА!")

    except ValueError:
        print("❌ Ошибка: вводите цену и количество только цифрами!")
        continue

# --- ВЫВОД ИТОГОВОГО ЧЕКА ---
print("\n" + "="*30)
print("ФИНАЛЬНЫЙ ОТЧЕТ:")
if not basket:
    print("Продаж сегодня не было.")
else:
    for position in basket:
        print(f"• {position}")

print("-" * 30)
print(f"ИТОГО К ОПЛАТЕ: {total_sum} руб.")
print("="*30)

# --- СОХРАНЕНИЕ В ФАЙЛ (Бонус для портфолио) ---
with open("report.txt", "a", encoding="utf-8") as file:
    file.write(f"\nОтчет от новой сессии. Итого: {total_sum} руб.")
    print("\n✅ Данные сохранены в файл report.txt")