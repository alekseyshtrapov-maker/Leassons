
with open('INPUT.TXT', 'r') as f:
    N = int(f.read().strip())

result = N + 1

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result))
