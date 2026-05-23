# Считываем данные из файла INPUT.TXT
with open('INPUT.TXT', 'r') as f:
    N, M, K = map(int, f.readline().split())

# Проверяем условие
if K >= N * M:
    result = "YES"
else:
    result ="NO"

# Записываем результат в файл OUTPUT.TXT
with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
    