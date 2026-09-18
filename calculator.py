def calculate_one_rep_max(weight, reps):
    # Формула Эпли для расчета одноповторного максимума
    if reps == 1:
        return weight
    return weight * (1 + reps / 30)

print("--- Калькулятор жима лежа ---")
try:
    weight = float(input("Введи рабочий вес штанги (кг): "))
    reps = int(input("Введи количество повторений: "))
    
    max_weight = calculate_one_rep_max(weight, reps)
    
    print(f"\nТвой примерный разовый максимум (1RM): {max_weight:.1f} кг")
except ValueError:
    print("Ошибка: пожалуйста, вводи только числа!")