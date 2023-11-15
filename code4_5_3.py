# allays = [10,9,8,7,6,5,4,3,2,1,"Lift Off !"]
# for count in allays:
#     print(count,end="")

for count in range(11):
    if count != 10:
        print(f"{10-count},",end = "")
        continue
    else:
        print("Lift off !")
        break