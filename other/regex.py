####
### Meta characters

# \ - drop special meaning of character following it
# [] - represent a character class
# ^ - matches the beginning
# $ - matches the end
# . - matches any character except new line
# | - matches with any of the characters separated by it
# ? - matches zero or one occurrence
# * - any number of occurrences (including 0)
# + - one or more occurrences
# {} - indicate the number of occurrences of a preceding RegEx to match
# () - enclose a group of RegEx

# Example
import re 
  
print(re.findall(r'[Gg]eeks', 'GeeksforGeeks: A computer science portal for geeks'))

# RegEx Search

grp = re.search(r'([\d]{2})-([\d]{2})-([\d]{4})','26-08-2020') 

# Compiled RegEx

regex = re.compile(r'([\d]{2})-([\d]{2})-([\d]{4})') 
  
print('compiled reg expr', regex.search('26-08-2020')) 

####
### Special sequences

# \A - matches is the string begins with the given character
# \b - matches if the word begins or ends with the given character
# \B - matches if the word does not begin or end with the given character
# \d - matches any decimal digit, this is equivalent to the set class [0-9]
# \D - matches any non-digit character, this is equivalent to the set class [^0-9]
# \s - matches any whitespace character
# \S - matches any non-whitespace character
# \w - matches any alphanumeric character, this is equivalent of the class [a-zA-Z0-9_]
# \W - matches any non-alphanumeric character
# \Z - matches if the string ends with the given regex