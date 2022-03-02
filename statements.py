print(5*6)
print(5+6)
print(3/2)
print(3-2)
print(5*6+12)
print((1+2)*3)

print("alma"+"körte") # konkatenálás

#str+int
#int+str
#str-kivonni másikat
#str*str
#str*int

n = 2
a ="alma"
#print( a + n) # TypeError: can only concatenate str (not "int") to str
#print(n + a) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print( a -"körte") # TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print( a *"körte") # TypeError: can't multiply sequence by non-int of type 'str'
print("alma"* n) # ez almaalma lesz

name = "John Doe"
message = "A name valtozo tipusa: " + str(type(name))
print(message)

hours = 3
minutes = hours * 60
print((((str(hours) + " óra az ")+ str (minutes)) + " perc " ))

word = "megszentségteleníthetetlenségeitekért"
print ("A" + word + " pontosan " + str (len(word))+ " karakter hosszú. ")

fruit = "alma"
print('gyumolcs: "'+ fruit + '"')

