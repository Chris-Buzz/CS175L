#CS175L
#Christopher Buzaid
#restaurant

print("Please respond to the following questions with a 'Yes'or 'No'")
vegetarian = str(input('Is anyone in your party vegetarian? '))
vegetarian = vegetarian.upper()
if vegetarian == 'YES':
    vegetarian = True
else:
    vegetarian = False
vegan = str(input('Is anyone in your party vegan? '))
vegan = vegan.upper()
if vegan == 'YES':
    vegan = True
else:
    vegan = False
gluten_free = str(input('Is anyone in your party gluten-free? '))
gluten_free = gluten_free.upper()
if gluten_free == 'YES':
    gluten_free = True
else:
    gluten_free = False
    
print('\nHere are your restaurant choices: ')
if vegan  and vegetarian and gluten_free == True:
    print("Corner Café \nThe Chef's Kitchen  ") 
elif gluten_free and vegan == True:
    print("Corner Café \nThe Chef's Kitchen  ") 
elif  vegan and vegetarian == True:
    print("Corner Café \nThe Chef's Kitchen  ") 
elif  vegetarian and gluten_free == True:
    print("Main Street Pizza Company \nCorner Café \nThe Chef’s Kitchen")
elif vegan == True:
    print("Corner Café \nThe Chef's Kitchen  ") 
elif vegetarian == True:
    print("Mama's Fine Italian \nMain Street Pizza Company \nCorner Café \nThe Chef's Kitchen  ") 
elif gluten_free == True:
   print("Main Street Pizza Company \nCorner Café \nThe Chef's Kitchen  ") 
else:
    print("Joes Gourmet Burgers \nMain Street Pizza Company \nCorner Café \nMama’s Fine Italian \nThe Chef’s Kitchen") 

    
