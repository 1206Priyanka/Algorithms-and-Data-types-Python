

#Declaring the initial values of the vaariables including a temporary variable
x0 =0
x1 = 1
x2 = 2
x3 =3
temp =-1


#shift the values of the variable in a circle 
temp =x0
x0=x1
x1 = x2
x2 = x3
x3 = temp


#print the new values of all the variables
print(x0,x1,x2,x3)
