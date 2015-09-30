
# check if entered is a palindrome

# Ask user to enter a word 
entered_word = raw_input("Enter a word: ")

# Reverse the entered word
rev_word = reversed(entered_word)

# Compare the strings
if list(entered_word) == list(rev_word):
	print("True")
else:
	print("False")