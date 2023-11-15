
count = 1
print("カレーを召し上がれ")
while True:
    print(f"{count}皿のカレーを食べました")
    more = input("おかわりはいかがですか？(y/n)>>")
    if more == "y":
        count += 1
        continue
    else:
        print("ごちそうさまでした")
        break
