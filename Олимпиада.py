def calculate_score(times, order):
    """
    Рассчитывает количество решённых задач и штрафное время
    для заданного порядка решения.
    Возвращает: (количество_задач, штрафное_время)
    """
    total_time = 0
    penalty = 0
    solved = 0

    for time in order:
        if total_time + time <= 300:
            total_time += time
            penalty += total_time
            solved += 1
        else:
            break

    return solved, penalty

# Чтение входных данных
with open('INPUT.TXT', 'r') as f:
    N = int(f.readline().strip())
    times = list(map(int, f.readline().split()))

# Порядок решения для каждого студента
senior_order = times  # пятикурсник: по порядку
junior_order = sorted(times)  # первокурсник: от простой к сложной
third_order = times[::-1]  # третьекурсник: в обратном порядке

# Расчёт результатов
senior_solved, senior_penalty = calculate_score(times, senior_order)
third_solved, third_penalty = calculate_score(times, third_order)
junior_solved, junior_penalty = calculate_score(times, junior_order)

# Формирование списка студентов с их результатами и приоритетом (младший курс — выше приоритет)
students = [
    (junior_solved, junior_penalty, 1),   # первокурсник
    (third_solved, third_penalty, 3),     # третьекурсник
    (senior_solved, senior_penalty, 5)   # пятикурсник
]

# Сортировка по правилам ACM:
# 1. Больше решённых задач
# 2. Меньше штрафного времени
# 3. Младший курс (уже учтён в порядке списка)
winner = max(students, key=lambda x: (x[0], -x[1], -x[2]))

# Запись результата
with open('OUTPUT.TXT', 'w') as f:
    f.write(str(winner[2]))
