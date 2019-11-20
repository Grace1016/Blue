#!/usr/bin/env python3
"""This is a script containing some practices in regex"""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

import re
my_string = "a given string"
match = re.search(r'\s',my_string)
print(match)
match.group()
match = re.search(r'\d',my_string)
print(match)
MyStr = 'an example'
match = re.search(r'\w*\s',MyStr)

if match:
    print('found a match:',match.group())
else:
    print('did not find a match')

match = re.search(r'2',"it takes 2 to tango")
match.group()

match = re.search(r'\d',"it takes 2 to tango")
match.group()

match = re.search(r'\d.*',"it takes 2 to tango")
match.group()

match = re.search(r'\s\w*$', 'once upon a time')
match.group()

#Let's switch to a more compact syntax by directly returning
#the matched group (by directly appending .group() to the result).

re.search(r'\w*\s\d.*\d','take 2 grams of H2O').group()
re.search(r'^\w*.*\s', 'once upon a time').group() # 'once upon a'
re.search(r'^\w*.*?\s', 'once upon a time').group()

#To further illustrate greediness in regexes, let's try matching an HTML tag:

re.search(r'<.+>', 'This is a <EM>first</EM> test').group()
re.search(r'<.+?>', 'This is a <EM>first</EM> test').group()
re.search(r'\d*\.?\d*','1432.75+60.22i').group()
re.search(r'[AGTC]+', 'the sequence ATTCGT').group()
re.search(r'\s+[A-Z]\w+\s\w+','The bird-shit frog''s name is Theloderma asper').group()

re.search(r'\d')