# Need to swap the values without using third variable 
a = 5 
b = 10 
print("The value a and b is ", a , b) 
a = a + b
b = a - b
a = a - b 

print("The new value a and b is ", a , b)

