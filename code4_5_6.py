numbers = [1, 1]
total = 0
while total <= 1000:
    total = 0
    total = numbers[-1]+numbers[-2]
    if total < 1000:
        numbers.append(total)
print(numbers)
ratius = []
for num in range(len(numbers)-1):
    sum1 = numbers[num + 1] / numbers[num]
    sum2 = int(sum1 * 1000)
    ans = sum2/1000
    ratius.append(ans)
print(ratius)
