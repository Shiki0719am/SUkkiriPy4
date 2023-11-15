temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]
for num in temp:
    print(num)
temp_new = [7.8, 9.1, 10.2, 11.0, 12.5, "N/A", 14.3, 13.8, 12.9, 12.4]
count1 = 0
for num1 in temp:
    count1 += 1
    count2 = 0
    for num2 in temp_new:
        count2 += 1
        if count1 == count2:
            if num1 != num2:
                print(f"違うのは{num1}と{num2}")
        elif count1 < count2:
            break

total = 0
temp_count = 0
for num in temp_new:
    if isinstance(num , float):
        total += num
        temp_count += 1
print(f"平均気温は{total / temp_count}")