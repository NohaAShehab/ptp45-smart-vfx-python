# num1 = input("please num1 : ")
# num2 = input("please enter num2: ")
# num1 = int(num1)
# num2 = int(num2)
# operation = input("please enter operation: ")  # string
# if operation == "+":
#     res = num1 + num2
#     print(res)
# elif operation == '-':
#     res = num1 - num2
#     print(res)
# elif operation == '*':
#     res = num1 * num2
#     print(res)
# elif operation == '/':
#     res = num1 / num2
#     print(res)
# else:
#     print("----- not valid operation ")









##problem 2
# value= ""
# counter = 0
# while value != "done":
#     value = input("please enter num: ")
#     counter +=1
#     print (counter, value)


# another solution
# value= ""
# counter = 0
# while value != "done":
#     value = input("please enter num: ")
#     counter +=1
#     print (value)
#     if value=='done':
#         print(counter)







####################################
# if you want to stop the loop ... break the loop # break


# while True:
#     num = input("please enter number ")
#     print(num)





result = 1
counter = 1

while True:
    usernum = input("please enter number: ")
    usernum = int(usernum)
    result *= usernum
    counter +=1
    if counter == 8:
        break

print(result)












