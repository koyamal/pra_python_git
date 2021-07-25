A, B = map(int, input().split())

output = 0
for number in range(A, B + 1):
    str_number = str(number)
    count_up = True
    for point_number in range(len(str_number) // 2):
        if str_number[point_number] != str_number[len(str_number) - point_number - 1]:
            count_up = False
            break
    if count_up:
        output += 1

print(output)
