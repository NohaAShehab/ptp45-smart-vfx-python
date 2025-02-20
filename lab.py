
# write a program that asks the user to enter any word and check if the char i
# located in this word or not.
# If the char i in the string prints its index.



anyword = input("Please enter any word: ")
# print(anyword)
# index = 0
# while index < len(anyword):
#     print(anyword[index])
#     # if anyword[index]=='i':
#     #     print("i found at index ", index)
#
#     index +=1




#
# word = input("please enter word ")
# index = 0
# newword=  ""
# while index < len(word):
#     char = word[index]
#     if char =="a" or char=='e' or char=="i" or char=='o' or char=='u':
#         print("Vowel found = "+ char)
#     else:
#         newword = newword + char
#     index +=1
#
# print("word after removing vowels= "+ newword)





#
#
# anystring = input("please enter the string ")
# # assume that nonvowelschar = 0  and vowelsChar = 0
# nonvowels =0
# vowelschar = 0
# # I need to loop the chars in the string so I need index = 0
# index = 0
# while index < len(anystring):
#     # pick the char
#     char = anystring[index]
#     # check if char in vowels ==> increment vowelschar else increment nonvowels
#     if char=='a' or char=='i' or char=='e' or char=='o' or char=='u':
#         vowelschar +=1
#     else:
#         nonvowels +=1
#
#     # then increment the index
#     index +=1
#
# print("number of vowels = " + str(vowelschar))
# print("number of nonvowels= " + str(nonvowels))



###########################################

anystring = "python"
index = len(anystring)-1  # 5 ---> 4 --> 3--> 2 -> 1-->0
newstring = ""  # nohtyp
while index > -1 :
    char = anystring[index]  # p
    newstring +=char
    index -=1

print(newstring)





































