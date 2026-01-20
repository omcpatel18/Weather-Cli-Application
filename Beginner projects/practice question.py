# aim = write a programm to find most repeating characyer in this text
sentence = " This is a common interview question"
# step 1 :- finding total alphabets use for writing this sentence.

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)