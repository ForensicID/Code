var_array = [i for i in range(101)]

total_sum = 0

for number in var_array:
    total_sum += number

result = total_sum / len(var_array)

print("Nilai rata-rata elemen array:", result)