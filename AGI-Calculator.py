#AGI Calculator  
#For calculating tenant rent amounts with various 
#above guideline increases, and city rent reductions.
#
#This is released under the GPL V2



# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

#Enter guideline amounts, agi's and rent reductions (if any)
print("Welcome to AGI-Calculator")
guideline = float(input("Please enter this year's guideline amount:"))
AGI1 = float(input("Please enter the approved AGI amount for the first year:  "))
AGI2 = float(input("Please enter the approved AGI amount for the second year:  "))
AGI3 = float(input("Please enter the approved AGI amount for the third year:  "))
reduction = float(input("Please enter the city rent reduction for this year:  "))
currentRent = float(input("Please enter the tenant's current rent:  "))



