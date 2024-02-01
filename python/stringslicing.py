
name = 'Rohan,Amanur'
# if we have to print the limited string then we use string slicing
print(name[0:6])
print(name[3:5])
print(name[2:5])                           

# to find the string length we use len statment
print(len(name))

# if we use negative slicing on after colon then
# it shows the length after substracting. Here the string lenght is 12 and after substrcting 5 it shows the 7 character of string
print(name[0:-5])
print(name[0:len(name)-5])

#if we use negative slicing on both side of colon
# it eliminates the 4 from front side and calculate the remaining string which is 8 and same as back side it calculate the remaining char after sub which is 11 so the output is in between [8:11]
print(name[-4:-1]) 

# here both show the same result
print(name[-9:len(name)-5])
print(name[3:7])
 