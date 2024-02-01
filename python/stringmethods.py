str = "Rohan Parbatani!!"
print(str.upper())

# the upper function will convert all the letter inn upper case

print(str.lower())

# the lower function will convert all the letter inn lower case 

print(str.strip)

# the strip func will remove the blank spaace

print(str.rstrip("!"))

# the rstrip func will remove the given trailing character

print(str.replace("Rohan Parbatani","hi"))

# the replace func will replace the all occurences of original string with the given string

print(str.split(" "))

# the split func will split the string between the space

a = "rohaN"

print(a.capitalize()) 

# the capitalize func will capitalize the first word of  the string and it converts the other of string  in  lower  case

print(str.center(35))

# the center func will mmove the  string to the center it will move spaces which was given in parentheses

print(str.count("a"))

# the count func will count the chararter or word in the parentheses

print(str.endswith("!"))

# the endswith func will justify that the string will end with the given char or not if it ends with given char then it shows true otherwise false

print(str.find("a"))

# the find func will find the first occerence of the given character in parentheses and prints its position

print(a.isalnum())

# the isalnum func return true only if the string consists of A-Z,a-z,0-9 if isalnum finds the special character in the string then it return false

print(a.isalpha)

# the isalpha func return true only if the string consists of A-Z,a-z if isalpha finds the special number in the string then it return false

print(a.islower())

# if all the character in thee string are in lower case then it return true otherwise false

print(a.isupper())

# if all the character in thee string are in upper case then it return true otherwise false

name = "Rohan\n"

print(name.isprintable())

# if all the character in thee string are printable then it return true otherwise false. It also returns true if the string is empty.in this case it returns false because of /n

print(str.isspace)

# if all the character in thee string are space then it return true otherwise false.

print(a.istitle)

# if all the first charaacter of the string is in upper case then it return true otherwise false.

print(a.isascii())

# if all the character in thee string are ascii then it return true otherwise false.

print(str.startswith("Rohan"))

# the startswith func will justify that the string will start with the given char or not if it starts with given char then it shows true otherwise false

print(a.swapcase("rohaN"))

# it will swap the upper case into lower case and lower case into upper case

print(str.title)

# it will capitalize the first letter of each word in the string.