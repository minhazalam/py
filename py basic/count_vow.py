# Count vowels

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# take input
str_input = input("Enter a string : ")

# count init
count = 0

# iteration
for char in str_input :
    if char in vowels :
        count += 1

# print total number of vowels in the string
print(count)