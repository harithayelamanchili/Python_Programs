# Program to count the number of words.

sen = raw_input("Enter a sentence:")
count = 0
for c in sen:
  if c in sen:
	count+= 1
	
print(count)
