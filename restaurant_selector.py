# This program asks the user whether any members of their party are vegetarian, vegan, or gluten-free, and
# displays restaurants that match the criteria.

# Ask the user if anyone in their party is vegetarian.
vegetarian = input('Is anyone in your party a vegetarian? ')

# Ask the user if anyone in their party is vegan.
vegan = input('Is anyone in your party a vegan? ')

# Ask the user if anyone in their party is gluten-free.
gluten_free = input('Is anyone in your party gluten-free? ')

# Display the restaurant options.
print('Here are your restaurant choices: ')
if vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'yes':
    print("Corner Café")
    print("The Chef's Kitchen")

elif vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'no':
    print("Corner Café")
    print("The Chef's Kitchen")

elif vegetarian == 'yes' and vegan == 'no' and gluten_free == 'yes':
    print("Main Street Pizza Company")
    print("Corner Café")
    print("The Chef's Kitchen")

elif vegetarian == 'yes' and vegan == 'no' and gluten_free == 'no':
    print("Main Street Pizza Company")
    print("Corner Café")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")

elif vegetarian == 'no' and vegan == 'yes' and gluten_free == 'yes':
    print("Corner Café")
    print("The Chef's Kitchen")

elif vegetarian == 'no' and vegan == 'no' and gluten_free == 'yes':
    print("Main Street Pizza Company")
    print("Corner Café")
    print("The Chef's Kitchen")

elif vegetarian == 'no' and vegan == 'yes' and gluten_free == 'no':
    print("Corner Café")
    print("The Chef's Kitchen")

# Display the result if all answers are no.
else:
    print("Joe's Gourmet Burgers")
    print("Main Street Pizza Company")
    print("Corner Café")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
