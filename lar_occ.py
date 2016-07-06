str = input("Enter a String:")
length = len( str )
check = str[0]
largest = ""

for i in range(1,length):
    if len(check) > len(largest):
        largest = check
    if str[i] >= str[i-1]:
        check = check + str[i]
    else:
        check = str[i];

print("largest occurrence of string in alphabetic order is :")
print(largest)
