# Считываем данные из файла INPUT.TXT
with open('INPUT.TXT', 'r') as f:
    H, L = map(int, f.readline().split())

# Рассчитываем количество непростреленных банок
harry_missed = L - 1
larry_missed = H - 1

# Записываем результаты в файл OUTPUT.TXT
with open('OUTPUT.TXT', 'w') as f:
    f.write(f"{harry_missed}{larry_missed}")
    