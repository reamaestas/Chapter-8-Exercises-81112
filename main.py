# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.
print(text[0:12])
print('--------------------------')

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
print(text[-12:])
print('--------------------------')

# 3. Print a slice of the middle 12 characters from 'text'.
print(text[12:24])
print('--------------------------')

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.

for char in word:
	print(char)
print('--------------------------')

for index in range(0, len(word)):
	print(word[index])
print('--------------------------')

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.

#this is reversed one letter on each line
for index in range(-1, len(word)-1):
	print(word[index])
print('--------------------------')


word_reversed = ""
for char in range(len(word)-1, -1, -1):
	word_reversed += word[char]
	
# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').