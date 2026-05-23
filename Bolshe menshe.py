with open('INPUT.TXT', 'r') as input_file:
    A = int(input_file.readline().strip())
    B = int(input_file.readline().strip())


if A < B:
    result = '<'
elif A > B:
    result = '>'
else:
    result = '='

with open('OUTPUT. TXT', 'w') as output_file:
    output_file.write(result)
