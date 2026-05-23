# Считаем данные из файла INPUT.TXT
# with open('enia.txt', 'r') as f:
#     N, A, B, = map(int, f. readline().split())

ввод = input()
# '4 11 22' -> ['4','11','22'] -> [4,11,22]
N, A, B =map(int, ввод.split())

# Рассчитаем вес сульфида
total_weight = N * A * B * 2

# Записываем результат в файл OUTPUT.TXT
# with open('OUTPUT.TXT', 'w') as f:
#     f.write(str(total_weight))
print(total_weight)