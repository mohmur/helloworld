str=input("Enter a string")
k=str.count('bob')
print("Number of occurances of bob is :")
print(k)
length = len(str)
count = 0

for i in range(0,length-2):
    if str[i:i+3] == "bob":
        count = count + 1
    

print("Number of occurences of bob is :")
print(count)
    
