is_awake = True
coumt = 0
while is_awake:
    coumt += 1
    print(f"ひつじが{coumt}匹")
    key = input("もう眠りそうですか？(y/n)>>")
    if key == "y":
        is_awake = False
print("おやすみなさい")