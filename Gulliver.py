# Считываем данные из файла INPUT.TXT
with open('INPUT.TXT', 'r') as f:
    K, M, = map(int, f.readine().split())

# Рассчитываем количество матраце
mattresses_count = K * K * K * M

# Записываем результат в файл OUTPUT.TXT
with open('OUTPUT.TXT', 'w') as f:
    f.write(str(mattresses_count))
    