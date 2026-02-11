temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

print("Wednesday:", temperatures[2])

maxt = 0
for temp in temperatures:
    if temp > maxt:
       maxt = temp

mint = 50
for temp in temperatures:
    if temp < mint:
       mint = temp

print("Max:", maxt)
print("Min:", mint)

total = 0
for temp in temperatures:
    total += temp
average = round(total / len(temperatures), 1)

print("Average:", average)

total_days = 0
for temp in temperatures:
    if temp > 17:
        total_days += 1

print("Days above 17:", total_days)
temperatures.sort()
print(temperatures)