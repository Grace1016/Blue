#!/usr/bin/env python3
"""print bird's latin name, common name and mass on separate lines"""

__author__=' Hongye Wang (hw2419@ic.ac.uk) '
__version__=' 0.0.1 '

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
        )

# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line or output block by species 
# Hints: use the "print" command! You can use list comprehensions!

# use loop and adjust the format of output
for tuple in birds:
    print("latin name:",tuple[0])
    print("common name:",tuple[1])
    print("mass:",tuple[2])

#use list comprehension
[print(bird) for bird in birds]