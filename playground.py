while True:
    num = input("please enter number ")
    if num.isdigit():
        num = int(num)
        break

    print("---- please enter valid number ----")


print("num = "+ str(num))
